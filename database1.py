import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
# can be set automatically to the name of the file.
# __file__ --> C://user/sid/desktop/myflaskexamples/basic.py

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#####################################################################################
# CREATING OUR FIRST MODEL

class Puppy(db.Model):