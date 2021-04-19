"""
Copyright (c)
Author: James Bennion-Pedley
Date: 2021 - present
Licence: MIT
"""

from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

# Create app and corresponding database
db = SQLAlchemy()
app = Flask(__name__)

# Set configs using environment variables
app.config['SECRET_KEY'] = environ.get('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Configure login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

# User login loader (Flask-login)
@login_manager.user_loader
def load_user(user_id):
	# since the user_id is just the primary key of our user table, use it in the query for the user
	return User.query.get(int(user_id))

# Create database if it doesn't exist
with app.app_context():
	db.create_all()

# Main blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

# Authentication blueprint
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

