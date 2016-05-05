#!/usr/bin/python
# Raspberry Pi Camera Rev v1.3

# THIS IS STILL IN DEVELOPMENT

import io, time, picamera

class Camera:

	def __init__(self):
		self.camera = picamera.PiCamera()
		self.stream = io.BytesIO()

	def stream_img(self):
		self.camera.start_preview()
		# Camera warm-up time
		time.sleep(2)
		self.camera.capture(self.stream, 'jpeg')
