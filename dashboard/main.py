"""
Copyright (c)
Author: James Bennion-Pedley
Date: 2021 - present
Licence: MIT
"""

# from dashboard import app

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

# Home page
@main.route('/')
@login_required
def index():
	return render_template('index.html')

