#!python

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = os.environ.get("SECRET_KEY") or "I_<3_Rusty_26-04-2020"
  
  