from flask import Flask, render_template, request, session, redirect, url_for
from classes.curso import Curso
import sqlite3
import logging
import os 

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

db_path = os.path.join(os.path.dirname(__file__), 'database.db')
logging.basicConfig(level=logging.DEBUG)

db_connection = sqlite3.connect(db_path)
db_cursor = db_connection.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/disciplinas')
def disciplinas():
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
    
@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404

@app.route('/contato', methods=['GET', 'POST'])
def enviar_contato():
    nome = request.form.get('nome')
    email = request.form.get('email')
    curso = request.form.get('disciplina')
    if not nome or not email or not curso:
        return render_template('contato.html', erro=True)
    else: return render_template('contato.html', sucesso=True, nome=nome)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'mudar123':
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            message = 'Credenciais inválidas. Tente novamente.'
            return render_template('login.html', message=message)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)