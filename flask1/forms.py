from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields import SubmitField, StringField, PasswordField, FileField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, ValidationError


class RegisterForm(FlaskForm):
    username = StringField(label=u'昵称', validators=[DataRequired()])
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("请输入邮箱！"),
            Email("邮箱格式不正确！")
        ])

    password = PasswordField(label=u'密码', validators=[DataRequired()])
    verify_password = PasswordField(label=u'确认密码', validators=[DataRequired(), EqualTo('password', message="两次密码不一致！")])
    submit = SubmitField(label=u'注册')