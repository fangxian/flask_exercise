from wtforms.fields import StringField, SubmitField, TextAreaField, SelectField, FileField, SelectMultipleField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError, EqualTo


class RegisterForm(FlaskForm):
    pass


class LoginForm(FlaskForm):
    pass


class EditProfileForm(FlaskForm):
    pass


class EditPwdForm(FlaskForm):
    pass
