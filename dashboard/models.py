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
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	name = db.Column(db.String(1000))
