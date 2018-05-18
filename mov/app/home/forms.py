from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, BooleanField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired
from app.models import User, Article

