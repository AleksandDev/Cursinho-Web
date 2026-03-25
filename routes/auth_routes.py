from flask import Blueprint, redirect, render_template, request, session, url_for
from models.bd import SessionLocal, hash_password
from models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
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
                return redirect(url_for("courses.home"))
            message = "Credenciais invalidas. Tente novamente."
            return render_template("login.html", message=message)
        finally:
            db.close()
    return render_template("login.html")


@auth_bp.route("/cadastro", methods=["GET", "POST"])
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


@auth_bp.route("/recuperar-senha", methods=["GET", "POST"])
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


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
