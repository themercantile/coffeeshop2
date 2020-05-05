#!python3

from flask import render_template, redirect, url_for, session
from app import app
from app.covform import CoffeeForm


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods = ["GET", "POST"])
def index():
  coffeeForm=CoffeeForm()
  if coffeeForm.validate_on_submit():
    #sessions in Flask allow you to access data outside the local scope
    session["coffeeData"] = [coffeeForm.drink_type.data, 
                          coffeeForm.milk_type.data, 
                          coffeeForm.sugar.data, 
                          coffeeForm.extras.data,
                          coffeeForm.email.data, 
                          coffeeForm.username.data,
                          coffeeForm.payment.data]
    return redirect(url_for("order"))
  return render_template("index.html", form=coffeeForm)

@app.route("/order", methods=["GET", "POST"])
def order():
  myData = session["coffeeData"]
  print(myData)
  return render_template("order.html", data=myData)
