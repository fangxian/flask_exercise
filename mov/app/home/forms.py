from wtforms.fields import StringField, SubmitField, TextAreaField, SelectField, FileField, SelectMultipleField, \
    PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError, EqualTo
from ..models import User


class RegisterForm(FlaskForm):
    name = StringField(label='昵称', validators=[DataRequired("请输入昵称")], description='昵称',
                       render_kw={"class": "form-control", "placeholder": "请输入昵称!"})
    email = StringField(label='邮箱', validators=[DataRequired("请输入邮箱")], description="邮箱",
                        render_kw={"class": "form-control", "placeholder": "请输入邮箱"})
    pwd = PasswordField(label=u'密码', validators=[DataRequired("请输入密码")], description="密码",
                        render_kw={"class": "form-control", "placeholder": "请输入密码！"})
    repwd = PasswordField(label=u'密码', validators=[DataRequired("请输入密码"), EqualTo('pwd', message="密码不一致")],
                           description="密码",
                           render_kw={"class": "form-control", "placeholder": "请输入密码！"})
    info = TextAreaField(label='简介', description="简介", render_kw={"class": "form-control", "placeholder": "请输入个人简介"})
    submit = SubmitField('注册', render_kw={"class": "btn btn-primary"})

    # 自定义检查规则 validate_字段名，Flask检查该字段时会对该函数一起进行调用
    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).first()
        if user is not None:
            raise ValidationError("昵称已经存在")

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).first()
        if user is not None:
            raise ValidationError("邮箱已经存在")


class LoginForm(FlaskForm):
    email = StringField(label=u'邮箱', validators=[DataRequired("请输入邮箱！")], description="邮箱",
                          render_kw={"class": "form-control", "placeholder": "请输入邮箱！"})
    pwd = PasswordField(label=u'密码', validators=[DataRequired("请输入密码")], description="密码",
                        render_kw={"class": "form-control", "placeholder": "请输入密码！"})
    submit = SubmitField('登陆', render_kw={"class": "btn btn-primary btn-block btn-flat"})

    def validate_account(self, field):
        email = field.data
        user = User.query.filter_by(email=email).first()
        if user is None:
            raise ValidationError("账号不存在！")


# TODO 更改密码表格
class EditPwdForm(FlaskForm):
    old_pwd = PasswordField(label=u'旧密码', validators=[DataRequired("请输入旧密码！")], description="旧密码",
                            render_kw={"class": "form-control", "placeholder": "请输入旧密码"})
    newpwd = PasswordField(label=u'新密码', validators=[DataRequired('请输入新密码！')], description='新密码',
                           render_kw={"class": "form-control", "placeholder": "请输入新密码！"})
    submit = SubmitField('编辑', render_kw={"class": "btn btn-primary"})


class EditProfileForm(FlaskForm):
    new_phone = StringField(label=u'手机号码', description='新号码',
                            render_kw={"class": "form-control", "placeholder": "请输入手机号码！"})
    new_info = TextAreaField(label=u'简介', description='简介', render_kw={"class": "form-control", "rows": 10})
    new_name = StringField(label=u'昵称', description='新昵称', render_kw={"class": "form-control", "placeholder": "新昵称"})
    new_icon = FileField(label=u'头像', description='新头像')
    submit = SubmitField('编辑', render_kw={"class": "btn btn-primary"})
