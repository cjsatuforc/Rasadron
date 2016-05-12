#!/usr/bin/env python
"""
Socket Server
"""

import socketio
import eventlet
from flask import Flask, render_template

sio = socketio.Server()
app = Flask(__name__)

@app.route('/')
def index():
	"""Serve the client-side application."""
	# return render_template('index.html')
	return 'RPI Server'

@sio.on('connect')
def connect(sid, environ):
	print("connect ", sid)

@sio.on('hello')
def message(sid, data):
	print("hello: ", data)
	sio.emit(sid, 'reply')

@sio.on('disconnect')
def disconnect(sid):
	print('disconnect ', sid)

if __name__ == '__main__':
	# wrap Flask application with engineio's middleware
	app = socketio.Middleware(sio, app)

	# deploy as an eventlet WSGI server
	eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8080)), app)
