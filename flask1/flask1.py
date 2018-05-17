from flask import Flask, flash, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, LoginForm
from flask_login import login_user
from datetime import datetime
import pymysql
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'register page'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flask1'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(20), unique=True, index=True)
    password = db.Column(db.String(20))
    add_time = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return 'user table'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(
                email=form.email.data,
                username=form.username.data,
                password=form.password.data
            )
            db.session.add(user)
            db.session.commit()
            flash(u'注册成功')
            return redirect(url_for('hello_world'))
        flash('email has been registered')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            if user.password == form.password.data:
                login_user(user)
                flash(u'登录成功')
                return redirect(url_for('hello_world'))
            else:
                flash(u'密码错误')
        else:
            flash(u'账号错误')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    pass


@app.route('/article_list')
def article_list():
    pass


@app.route('/add_article')
def add_article():
    pass


if __name__ == '__main__':
    db.create_all()
    app.run()
