from . import render_template, redirect,url_for,abort,request
from . import main
from app.requests import get_quote
from flask_login import login_required,current_user
from ..models import Role,User,Blog,Comment,Subscriber
from ..import db, photos
import secrets
import os
from PIL import Image
from .forms import UpdateProfile,CreateBlog,CommentForm
from ..email import mail_message


#Views
@main.route('/')
def index():
    quote = get_quote()
    blogs = Blog.query.order_by(Blog.time.desc())
    return render_template('index.html', blogs=blogs,quote = quote)