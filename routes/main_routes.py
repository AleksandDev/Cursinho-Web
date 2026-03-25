from flask import Blueprint, redirect, render_template, request, session, url_for
from models.bd import SessionLocal, hash_password
from models.curso import Curso
from models.user import User
from routes.send_email import enviar_email

main_bp = Blueprint("main", __name__)

def _obter_curso(curso_nome):
    cursos = {
        "desenvolvimento-web": {
            "nome": "Desenvolvimento Web",
            "descricao": "Aprenda a criar sites e aplicacoes web do zero.",
            "duracao": "80 horas",
            "imagem_url": "/static/src/images/web.png",
            "habilidades": [
                "HTML",
                "CSS",
                "JavaScript",
                "Frameworks Front-end",
                "Nocoes de Back-end",
            ],
        },
        "programacao-orientada-a-objetos": {
            "nome": "Programacao Orientada a Objetos com Python",
            "descricao": "Domine os conceitos de POO usando Python.",
            "duracao": "60 horas",
            "imagem_url": "/static/src/images/python.png",
            "habilidades": [
                "Conceitos de POO",
                "Classes e Objetos",
                "Heranca",
                "Polimorfismo",
                "Encapsulamento",
            ],
        },
        "data-science": {
            "nome": "Data Science",
            "descricao": "Aprenda a analisar e interpretar dados.",
            "duracao": "100 horas",
            "imagem_url": "/static/src/images/data-science-1.webp",
            "habilidades": [
                "Analise de Dados",
                "Visualizacao de Dados",
                "Estatistica",
                "Machine Learning",
            ],
        },
    }

    dados = cursos.get(curso_nome)
    if not dados:
        return None

    curso = Curso(dados["nome"], dados["descricao"], dados["duracao"])
    curso.imagem_url = dados["imagem_url"]
    curso.habilidades = dados["habilidades"]
    return curso

@main_bp.route("/")
def home():
    if not session.get("logged_in"):
        return redirect(url_for("main.login"))
    return render_template("index.html")

@main_bp.route("/disciplinas")
def disciplinas():
    if not session.get("logged_in"):
        return redirect(url_for("main.login"))
    return render_template("disciplinas.html")

@main_bp.route("/curso/<curso_nome>")
def info_curso(curso_nome):
    curso = _obter_curso(curso_nome)
    if not curso:
        return "Pagina nao encontrada", 404
    return render_template("curso.html", curso=curso)

@main_bp.route("/contato", methods=["GET", "POST"])
def enviar_contato():
    if request.method == "GET":
        return render_template("contato.html", sucesso=False)

    nome = request.form.get("nome")
    email = request.form.get("email")
    curso = request.form.get("disciplina")

    if not nome or not email or not curso:
        mensagem = "Todos os campos sao obrigatorios."
        return render_template("contato.html", sucesso=False, mensagem=mensagem)

    enviar_email(email, "Contato Recebido - Cursinho Web", curso)
    return render_template(
        "contato.html",
        sucesso=True,
        nome=nome,
        email=email,
        curso=curso,
    )

@main_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.username == username).first()
            if user and user.check_password(password):
                session["logged_in"] = True
                session["username"] = username
                return redirect(url_for("main.home"))
            message = "Credenciais invalidas. Tente novamente."
            return render_template("login.html", message=message)
        finally:
            db.close()
    return render_template("login.html")

@main_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        db = SessionLocal()
        try:
            if db.query(User).filter(User.username == username).first():
                return render_template("cadastro.html", message="Nome de usuario ja existe.")
            if db.query(User).filter(User.email == email).first():
                return render_template("cadastro.html", message="Email ja cadastrado.")

            new_user = User(username=username, password=hash_password(password), email=email)
            db.add(new_user)
            db.commit()
            return render_template("login.html", message="Cadastro realizado com sucesso! Faca login.")
        finally:
            db.close()
    return render_template("cadastro.html", cadastro=True)

@main_bp.route("/recuperar-senha", methods=["GET", "POST"])
def recuperar_senha():
    if request.method == "POST":
        username = request.form.get("username")
        new_password = request.form.get("new_password")
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.username == username).first()
            if user:
                user.password = hash_password(new_password)
                db.commit()
                return render_template("login.html", message="Senha recuperada com sucesso!")
            return render_template("cadastro.html", message="Usuario nao encontrado.")
        finally:
            db.close()
    return render_template("cadastro.html", cadastro=False)

@main_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.login"))