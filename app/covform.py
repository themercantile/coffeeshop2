#!python3 Coffee Input Form

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, RadioField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email

class CoffeeForm(FlaskForm):
  username = StringField("Your Name", validators=[Length(min=2, max=30), DataRequired()])
  #email = EmailField('Email', [validators.Length(min=6, max=50), validators.Email()])  <-- Example from Reddit
  email = EmailField("Email", validators=[Length(min=6, max=40), Email(message=("Not a valid email address")), DataRequired()])
  drink_type = RadioField("Drink", choices=[("5.00", "Flat White"), ("5.00", "Cappucino"), ("4.80", "Black Coffee"), ("5.20", "Mocha"), ("5.50", "Hot Chocolate")])
  milk_type = SelectField("Milk", choices=[("None", "None"), ("Full Cream", "Full Cream"), ("Hi-Lo", "Hi-Lo"), ("Skim", "Skim"), ("Almond", "Almond"), ("Soy", "Soy")])
  sugar = SelectField("Sugar", choices=[("None", "None"), ("One", "One"), ("Two", "Two"), ("Three", "Three")])
  extras = SelectField("Extras", choices=[("None", "None"), ("Extra Shot", "Extra Shot"), ("Marshmallow", "Marshmallow"), ("Naked Sukes", "Naked Sukes")])
  payment = BooleanField("Paid")
  submit = SubmitField("Submit Order")