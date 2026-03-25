from flask import Blueprint, redirect, render_template, session, url_for
from models.curso import Curso

courses_bp = Blueprint("courses", __name__)

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

@courses_bp.route("/")
def home():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("index.html")


@courses_bp.route("/disciplinas")
def disciplinas():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("disciplinas.html")

@courses_bp.route("/curso/<curso_nome>")
def info_curso(curso_nome):
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))

    curso = _obter_curso(curso_nome)
    if not curso:
        return "Pagina nao encontrada", 404
    return render_template("curso.html", curso=curso)