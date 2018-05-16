from flask import Flask, flash, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm
from models import User
from flask_login import login_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'register page'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(form.email.data).first()
        if user is None:
            user.email = form.email.data
            user.username = form.username.data
            user.password = form.password.data
            db.session.add(user)
            db.session.commit()
            flash(u'注册成功')
            return redirect(url_for('hello_world'))
        flash('email has been registered')
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
