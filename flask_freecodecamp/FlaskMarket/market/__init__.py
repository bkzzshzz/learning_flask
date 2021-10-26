from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' 
# This is the key - SQLALCHEMY_DATABASE_URI; URI = Uniform Resource Identifier
app.config['SECRET_KEY'] = 'bbdf39c755e204a1ecfad191'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes
