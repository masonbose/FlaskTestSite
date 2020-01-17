# Tells system that this is package & init's everything 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config stuff
app = Flask(__name__)
app.config['SECRET_KEY'] = '67d345fd46e319b922b5073b610356ea'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# DB Instance
db = SQLAlchemy(app)

# import it here to avoid circular imports
from flaskblog import routes
