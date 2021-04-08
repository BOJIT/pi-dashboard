"""
Copyright (c)
Author: James Bennion-Pedley
Date: 2021 - present
Licence: MIT
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Load components
import dashboard.main
import dashboard.auth

