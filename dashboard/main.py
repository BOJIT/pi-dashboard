"""
Copyright (c)
Author: James Bennion-Pedley
Date: 2021 - present
Licence: MIT
"""

from dashboard import app
from flask import render_template

# Home page
@app.route('/')
def home():
	return render_template('index.html')

# Login page
