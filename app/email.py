from flask_mail import Message
from flask import render_template
from . import Mail

def mail_message(subject,template,to,**kwargs):
  sender_email = 'ngetij.nick@gmail.com'
  email = Message(subject, sender=sender_email, recipients=[to])
  email.body= render_template(template + ".txt",**kwargs)
  email.html = render_template(template + ".html",**kwargs)
  Mail.send(email)