#!python3

from flask import render_template
from app import app
from app.covform import CoffeeForm

@app.route("/")
@app.route("/index")
def index():
  coffeeForm=CoffeeForm()
  return render_template("index.html")