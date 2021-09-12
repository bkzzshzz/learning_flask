from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' 
# This is the key - SQLALCHEMY_DATABASE_URI; URI = Uniform Resource Identifier
app.config['SECRET_KEY'] = 'bbdf39c755e204a1ecfad191'
db = SQLAlchemy(app)

from market import routes
