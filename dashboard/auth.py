"""
Copyright (c)
Author: James Bennion-Pedley
Date: 2021 - present
Licence: MIT
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)


#------------------------------------- PAGES ----------------------------------#

# Login page
@auth.route('/login')
def login():
	return render_template('login.html')

# Logout page
@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))


#------------------------------------- POST -----------------------------------#

# Login POST
@auth.route('/login', methods=['POST'])
def login_post():
	username = request.form.get('username')
	password = request.form.get('password')
	remember = True if request.form.get('remember') else False

	user = User.query.filter_by(username=username).first()

	# check if user actually exists - if not redirect to login
	if not user or not check_password_hash(user.password, password): 
		flash('Please check your login details and try again.')
		return redirect(url_for('auth.login'))

	# if the above check passes, then we know the user has the right credentials
	login_user(user, remember=remember)
	return redirect(url_for('main.index'))
