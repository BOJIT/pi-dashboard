"""
Copyright (c)
Author: James Bennion-Pedley
Date: 2021 - present
Licence: MIT
"""

from os import environ
from flask import Flask
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Default credentials (created if no login exists). User cannot be deleted
default_username = 'admin'
default_password = 'pi_dashboard'

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
	return User.query.get(int(user_id))

# Create database if it doesn't exist
with app.app_context():
	db.create_all()

	# Create default admin user if one doesn't exist
	user = User.query.filter_by(username=default_username).first()

	if not user:
		new_user = User(username=default_username,
		                password=generate_password_hash(default_password,
		                method='sha256'),
		                is_admin=False)

		# add the new user to the database
		db.session.add(new_user)
		db.session.commit()

# Main blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

# Authentication blueprint
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

