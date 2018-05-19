from .forms import RegisterForm, LoginForm, EditProfileForm, EditPwdForm
from flask import render_template, redirect, url_for, flash, session
from . import home
from ..models import User
from werkzeug.security import generate_password_hash
from app import db


# 登录装饰器
def login_req(f):
    pass


@home.route('/')
def index():
    return render_template('home/welcome.html')


@home.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            name=data['name'],
            email=data['email'],
            info=data['info'],
            pwd=generate_password_hash(data['pwd'])
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功")
        return redirect(url_for('login'))
    return render_template('home/register.html', form=form)


@home.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(email=data['account']).first()
        if user is None or not user.check_pwd(data['pwd']):
            flash("账号或密码错误！")
            return redirect(url_for('home.login'))
        session["user"] = user.name
        session["user_id"] = user.id
        return redirect(url_for('index'))
    return render_template('home/login.html', form=form)


@home.route('/logout')
@login_req
def logout():
    pass


@home.route('/add_article', methods=['GET', 'POST'])
@login_req
def add_article():
    pass


@home.route('/del_article/<int:id>', methods=['GET', 'POST'])
@login_req
def del_article(id):
    pass


@home.route('/edit_article/<int:id>', methods=['GET', 'POST'])
@login_req
def edit_article(id):
    pass


@home.route('/article/<int:id>/add_comment', methods=['GET', 'POST'])
@login_req
def add_comment(id):
    pass
