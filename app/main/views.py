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

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    user = User.query.filter_by(username = name).first()
    form = UpdateProfile()
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.bio = form.bio.data
        db.session.commit()
        return redirect(url_for('main.profile',name=user.username,))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.bio.data = current_user.bio
    return render_template('profile/update.html', user = user, form =form)