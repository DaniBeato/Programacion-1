from .. import mailsender
from flask import current_app, render_template
from flask_mail import Message
from smtplib import SMTPException

def sendMail(to, subject, template, **kwargs):
    msg = Message(subject, sender = current_app.config['FLASKY_MAIL_SENDER'], recipients=to)
    try:
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = render_template(template + '.html', **kwargs)
        result = mailsender.send(msg)
    except SMTPException as e:
        print(str(e))
        return "Falló el envío del mail "
    return True



def enviar_ofertas(destinatario, asunto, template, **kwargs):
    msg = Message(asunto, sender = current_app.config['FLASKY_MAIL_SENDER'], recipients = destinatario)
    try:
        msg.body = render_template(template + '.txt', **kwargs)
        resultado = mailsender.send(msg)
    except SMTPException as e:
        print(str(e))
        return "Falló el envío del mail "
    return True