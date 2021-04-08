"""
Copyright (c)
Author: James Bennion-Pedley
Date: 2021 - present
Licence: MIT
"""

# Use waitress to serve Flask application on Production
from waitress import serve

# Flask application itself lives entirely in a module
from dashboard import app

# Log everything to the console in debug mode
# if __debug__:
# 	import logging
# 	logger = logging.getLogger('waitress')
# 	logger.setLevel(logging.INFO)

# Serve website - blocks indefinitely
if __debug__:
	app.run(debug=True)
else:
	serve(app, host='0.0.0.0', port=5000)
