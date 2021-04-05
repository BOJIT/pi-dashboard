"""
Copyright (c)
Author: James Bennion-Pedley
Date: 2021 - present
Licence: MIT
"""

# Use waitress to serve Flask application
from waitress import serve

# Flask application itself lives entirely in a module
from app import app

# Log everything to the console in debug mode
if __debug__:
	import logging
	logger = logging.getLogger('waitress')
	logger.setLevel(logging.INFO)

# Serve website - blocks indefinitely
serve(app, host='0.0.0.0', port=8080)
