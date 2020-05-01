#!python3 Coffee Input Form

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email

class CoffeeForm(FlaskForm):
  username = StringField("Your Name", validators=[Length(min=2, max=30), DataRequired()])
  #email = EmailField('Email', [validators.Length(min=6, max=50), validators.Email()])  <-- Example from Reddit
  email = EmailField("Email", validators=[Length(min=6, max=40), Email(message=("Not a valid email address")), DataRequired()])
  drink_type = SelectField("Name yer poison", choices=[("flatWhite", "Flat White"), ("cappucino", "Cappucino"), ("black", "Black"), ("mocha", "Mocha"), ("hotChoc", "Hot Chocolate")])
  milk_type = SelectField("Milk", choices = [("fullCream", "Full Cream"), ("hilo", "Hi-Lo"), ("skim", "Skim"), ("almond", "Almond"), ("soy", "Soy"), ("none", "None")])
  sugar = SelectField("Sugar", choices = [("one", "One"), ("two", "Two"), ("three", "Three"), ("none", "None")])
  payment = BooleanField("Paid")
  submit = SubmitField("Submit Order")
