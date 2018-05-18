from wtforms.fields import StringField, SubmitField, TextAreaField, SelectField, FileField, SelectMultipleField, \
    PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError, EqualTo
from ..models import User


class RegisterForm(FlaskForm):
    pass


class LoginForm(FlaskForm):
    account = StringField(label=u'账号', validators=[DataRequired("请输入账号！")], description="账号",
                          render_kw={"class": "form-control", "placeholder": "请输入账号！"})
    pwd = PasswordField(label=u'密码', validators=[DataRequired("请输入密码")], description="密码",
                        render_kw={"class": "form-control", "placeholder": "请输入密码！"})
    submit = SubmitField('登陆', render_kw={"class": "btn btn-primary btn-block btn-flat"})

    def validate_account(self, field):
        account = field.data
        user = User.query.filter_by(email=account).first()
        if user is None:
            raise ValidationError("账号不存在！")


# TODO 更改密码表格
class EditProfileForm(FlaskForm):
    old_pwd = PasswordField(label=u'旧密码', validators=[DataRequired("请输入旧密码！")], description="旧密码",
                            render_kw={"class": "form-control", "placeholder": "请输入旧密码"})


class EditPwdForm(FlaskForm):
    pass
