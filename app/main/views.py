from flask import render_template, redirect, url_for,abort,request
from . import main
from app.requests import get_quote
from flask_login import login_required,current_user
from ..models import User,Quote
from ..import db

import os


from ..email import mail_message



#Views
@main.route('/')
def index():
    '''
    main
    '''
    return render_template('index.html')
@main.route('/quotes')
def quotes():

    '''
    '''
    quote = get_quote()
    title = 'LetsBlog | Quotes'
    
    return render_template('quotes.html', title = title,quote = quote)