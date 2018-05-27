from .forms import RegisterForm, LoginForm, EditProfileForm, EditPwdForm, ArticleForm
from flask import render_template, redirect, url_for, flash, session, request
from . import home
from ..models import User, Article
from werkzeug.security import generate_password_hash
from app import db
from functools import wraps


# 登录装饰器
def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("home.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@home.route('/')
def index():
    return render_template('home/user.html')


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
        flash("注册成功", "ok")
        return redirect(url_for('home.index'))
    return render_template('home/register.html', form=form)


@home.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_pwd(data['pwd']):
            session["user"] = user.name
            session["user_id"] = user.id
            return redirect(url_for('home.index'))
        flash("账号或密码错误", "err")
        return redirect(url_for('home.login'))
    return render_template('home/login.html', form=form)


@home.route('/logout')
@user_login_req
def logout():
    session.pop("user", None)
    session.pop("user_id", None)
    return redirect(url_for("home.index"))


@home.route('/edit_pwd', methods=['GET', 'POST'])
@user_login_req
def edit_pwd():
    form = EditPwdForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=session['user']).first()
        if user.pwd != data['old_pwd']:
            flash("旧密码错误！", "err")
            redirect(url_for("edit_pwd"))
        if user.pwd == data['new_pwd']:
            flash("新旧密码一样", 'error')
            return redirect(url_for("edit_pwd"))
        user.pwd = data['new_pwd']
        db.session.add(user)
        db.session.commit()
        flash("密码更新成功", "ok")
        return redirect(url_for("home.index"))
    return render_template("home/edit_pwd.html", form=form)


@home.route('/edit_profile', methods=['GET', 'POST'])
@user_login_req
def edit_profile():
    form = EditProfileForm()
    user = User.query.filter_by(name=session['user']).first()
    if request.method == 'GET':
        form.new_name.data = user.name
        form.new_phone.data = user.phone
        form.new_info.data = user.info
        form.new_icon = user.icon
    if form.validate_on_submit():
        data = form.data
        if data['new_phone'] != user.phone and User.query.filter_by(data['new_phone']) is not None:
            flash("该号码已经被使用", "err")
            return redirect(url_for('home.edit_profile'))
        user.phone = data['new_phone']
        user.icon = data['new_icon']
        user.info = data['new_info']
        if data['new_name'] != user.name and User.query.filter_by(data['new_name']) is not None:
            flash("该昵称已经被使用", "err")
            return redirect(url_for('home.edit_profile'))
        user.name = data['new_name']
        db.session.add(user)
        db.session.commit()
        session['user'] = user.name
        flash("用户资料更新成功", 'ok')
        return redirect(url_for('home.edit_profile'))
    return render_template('home/edit_profile.html', form=form, user=user)


@home.route('/article_list')
# @user_login_req
def article_list():
    return render_template("home/art_list.html")


@home.route('/add_article', methods=['GET', 'POST'])
# @user_login_req
def add_article():
    form = ArticleForm()
    if form.validate_on_submit():
        data = form.data
        article = Article(
            title=data['title'],
            user_id=session['user_id'],
            content=data['body'],
            url=data['icon']
        )
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('home.article_list'))
    return render_template("home/add_article.html", form=form)


@home.route('/del_article/<int:id>', methods=['GET', 'POST'])
@user_login_req
def del_article(id):
    pass


@home.route('/edit_article/<int:id>', methods=['GET', 'POST'])
@user_login_req
def edit_article(id):
    pass


@home.route('/article/<int:id>/add_comment', methods=['GET', 'POST'])
@user_login_req
def add_comment(id):
    pass
