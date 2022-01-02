"""
Copyright (c)
Author: James Bennion-Pedley
Date: 2021 - present
Licence: MIT
"""

from flask_login import UserMixin
from . import db

# Basic user database entry structure
class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(1000), unique=True)
	password = db.Column(db.String(100))
	is_admin = db.Column(db.Boolean)
	dark_mode = db.Column(db.Boolean)
