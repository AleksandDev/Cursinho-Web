from flask import Flask, render_template, request, session, redirect, url_for
from models.bd import Base, Curso
from models.user import User
from models.bd import SessionLocal, create_tables, hash_password
import logging
from email.mime.text import MIMEText
import smtplib

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

create_tables()

db = SessionLocal()
try:
    if not db.query(User).filter(User.username == 'admin').first():
        default_user = User(username='admin', password=hash_password('mudar123'), email='admin@example.com')
        db.add(default_user)
        db.commit()
finally:
    db.close()

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/disciplinas')
def disciplinas():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('disciplinas.html')

@app.route('/curso/<curso_nome>')
def info_curso(curso_nome):
    if curso_nome == 'desenvolvimento-web':
        habilidades = ['HTML', 'CSS', 'JavaScript', 'Frameworks Front-end', 'Noções de Back-end']
    elif curso_nome == 'programacao-orientada-a-objetos':
        habilidades = ['Conceitos de POO', 'Classes e Objetos', 'Herança', 'Polimorfismo', 'Encapsulamento']
    elif curso_nome == 'data-science':
        habilidades = ['Análise de Dados', 'Visualização de Dados', 'Estatística', 'Machine Learning']

    curso = None
    if curso_nome == 'desenvolvimento-web':
        curso = Curso('Desenvolvimento Web', 'Aprenda a criar sites e aplicações web do zero.', '80 horas')
    elif curso_nome == 'programacao-orientada-a-objetos':
        curso = Curso('Programação Orientada a Objetos com Python', 'Domine os conceitos de POO usando Python.', '60 horas')
    elif curso_nome == 'data-science':
        curso = Curso('Data Science', 'Aprenda a analisar e interpretar dados.', '100 horas')
    
    if curso:
        curso.habilidades = habilidades
        return render_template('curso.html', curso=curso)
    else:
        return render_template('404.html'), 404

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404

def enviar_email(destinatario, assunto, curso):
    remetente = 'youremail@gmail.com'
    senha = 'inserir_senha_app'
    nome_destinatario = request.form.get('nome')
    informacoes = {'interesse': request.form.get('disciplina'),
        'linguagens': request.form.get('linguagens'),
        'conheceu': request.form.get('conheceu')}
    mensagem = request.form.get('mensagem')
    html = f"""
    <html>
    <body>
        <h1>Olá {nome_destinatario}! Obrigado por entrar em contato!</h1>
        <p>Recebemos sua mensagem e responderemos o mais breve possível.</p>
        <p>Detalhes: {informacoes}</p>
        <p>Mensagem: {mensagem}</p>
        <p>Atenciosamente,</p>
        <p>Cursinho Web</p>
    </body>
    </html>
    """
    msg = MIMEText(html, 'html')
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remetente, senha)

    servidor.sendmail(remetente, destinatario, msg.as_string())
    servidor.quit()

@app.route('/contato', methods=['POST', 'GET'])
def enviar_contato():
    nome = request.form.get('nome')
    email = request.form.get('email')
    curso = request.form.get('disciplina')
    mensagem = 'Todos os campos são obrigatórios.'
    if not nome or not email or not curso:
        return render_template('contato.html', sucesso=False, mensagem=mensagem)

    enviar_email(email, 'Contato Recebido - Cursinho Web', curso)

    return render_template(
        'contato.html',
        sucesso=True,
        nome=nome,
        email=email,
        curso=curso
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.username == username).first()
            if user and user.check_password(password):
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('home'))
            else:
                message = 'Credenciais inválidas. Tente novamente.'
                return render_template('login.html', message=message)
        finally:
            db.close()
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        db = SessionLocal()
        try:
            if db.query(User).filter(User.username == username).first():
                return render_template('cadastro.html', message='Nome de usuário já existe.')
            if db.query(User).filter(User.email == email).first():
                return render_template('cadastro.html', message='Email já cadastrado.')
            hashed_password = hash_password(password)
            new_user = User(username=username, password=hashed_password, email=email)
            db.add(new_user)
            db.commit()
            return render_template('login.html', message='Cadastro realizado com sucesso! Faça login.')
        finally:
            db.close()
    return render_template('cadastro.html', cadastro=True)

@app.route('/recuperar-senha', methods=['GET', 'POST'])
def recuperar_senha():
    if request.method == 'POST':
        username = request.form.get('username')
        new_password = request.form.get('new_password')
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.username == username).first()
            if user:
                user.password = hash_password(new_password)
                db.commit()
                return render_template('login.html', message='Senha recuperada com sucesso!')
            else:
                return render_template('cadastro.html', message='Usuário não encontrado.')
        finally:
            db.close()
    return render_template('cadastro.html', cadastro=False)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)