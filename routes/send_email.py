import smtplib
from flask import render_template, request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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