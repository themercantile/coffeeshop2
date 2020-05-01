#!python3 Coffee Input Form

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email

class CoffeeForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired()])
  #email = EmailField('Email', [validators.Length(min=6, max=50), validators.Email()])  <-- Example from Reddit
  email = EmailField("Email", validators=[Length(min=6, max=50), Email(message=("Not a valid email address"))])
  payment = BooleanField("Paid")
  submit = SubmitField("Sign In")
