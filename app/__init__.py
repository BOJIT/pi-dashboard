"""
Copyright (c)
Author: James Bennion-Pedley
Date: 2021 - present
Licence: MIT
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'
