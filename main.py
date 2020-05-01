#!python3
''' The purpose of this program will be to take orders of coffee. 
  It will have a header and a form with the following fields:
  Beverage Type, Milk, Sugar, Extras, Name, Email Address
  Payment will be through PayID. This will be provided within the web page.'''

from app import app

if __name__ == "__main__":
  app.run(debug=True)
