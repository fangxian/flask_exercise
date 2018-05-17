from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
from wtforms.fields import SubmitField, StringField, PasswordField, FileField, TextAreaField, SelectField
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


class LoginForm(FlaskForm):
    email = StringField(label=u'邮箱', validators=[DataRequired('输入邮箱'), Email(u'邮箱格式不对')])
    password = StringField(label=u'密码', validators=[DataRequired()])
    submit = SubmitField(label=u'登录')


class EditArticleForm(FlaskForm):
    title = StringField(label=u'标题', validators=[DataRequired()])
    cate = SelectField(label=u'分类选择', choices=[u'科技', u'搞笑', u'情感'])
    # 富文本编辑
    body = TextAreaField(label=u'文章内容', validators=[DataRequired()])
    submit = SubmitField(label=u'提交')
