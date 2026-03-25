import smtplib
from flask import render_template, request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

def enviar_email(destinatario, assunto, curso):
    remetente = os.getenv('EMAIL')
    senha = os.getenv('SMTP_APP_PASSWORD')
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
        <img src="https://i.postimg.cc/P50B06TB/Logo-do-Cursinho-Web-em-verde.png" alt="Email Image" style="width:300px;"> 
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

    mensagem = "Contato enviado com sucesso!"
    servidor.sendmail(remetente, destinatario, msg.as_string())
    servidor.quit()