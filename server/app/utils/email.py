from flask import current_app
from flask_mail import Message
from .. import mail
    

def email_sender(to_email, subject, body, is_html=False):
    sender = (current_app.config['MAIL_NAME'], current_app.config['MAIL_USERNAME'])
    msg = Message(subject, sender=sender, recipients=[to_email])
    if is_html:
        msg.html = body 
    else:
        msg.body = body
    mail.send(msg) 
    
def csv_email_sender(to_email, subject, body, csv_attachment):
    sender = (current_app.config['MAIL_NAME'], current_app.config['MAIL_USERNAME'])
    msg = Message(subject, sender=sender, recipients=[to_email])
    msg.html = body
    msg.attach("reservation_records.csv", "text/csv", csv_attachment)
    mail.send(msg)


def pdf_email_sender(to_email, subject, body, pdf_attachment):
    sender = (current_app.config['MAIL_NAME'], current_app.config['MAIL_USERNAME'])
    msg = Message(subject, sender=sender, recipients=[to_email])
    msg.html = body
    msg.attach("test.pdf", "application/pdf", pdf_attachment)
    mail.send(msg)
    