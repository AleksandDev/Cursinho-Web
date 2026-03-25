from flask import Blueprint, render_template, request
from routes.send_email import enviar_email
contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/contato", methods=["GET", "POST"])
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
