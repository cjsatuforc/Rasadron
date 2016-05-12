#!/usr/bin/env python
"""
Web Server - Serving Gyro, Temperature etc. data and motor controls
"""

import json
import web  # web.py

urls = ('/', 'index')

app = web.application(urls, globals())

class index:

	def GET(self):
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		return json.dumps({'status': False})

if __name__ == "__main__":
	app.run()
