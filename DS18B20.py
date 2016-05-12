#!/usr/bin/python
"""
Temperature Sensor - DS18B20
"""

import os, glob, time, subprocess

class Temperature:

	def __init__(self):
		os.system('modprobe w1-gpio')
		os.system('modprobe w1-therm')
		self.base_dir = '/sys/bus/w1/devices/'
		self.device_folder = glob.glob(self.base_dir + '28*')[0]
		self.device_file = self.device_folder + '/w1_slave'
		self.celsius = 0
		self.fahrenheit = 0

	def read_temp_raw(self):
		d_file = open(self.device_file, 'r')
		lines = d_file.readlines()
		d_file.close()
		return lines

	# if the above read_temp_raw doesnt work, try this
	# def read_temp_raw(self):
	# 	catdata = subprocess.Popen(['cat',device_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# 	out,err = catdata.communicate()
	# 	out_decode = out.decode('utf-8')
	# 	lines = out_decode.split('\n')
	# 	return lines

	def read_temp(self, mode):
		lines = self.read_temp_raw()
		while lines[0].strip()[-3:] != 'YES':
			time.sleep(0.2) # Remove this later ?
			lines = self.read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string) / 1000.0
			temp_f = temp_c * 9.0 / 5.0 + 32.0
			self.celsius = temp_c
			self.fahrenheit = temp_f
			if mode == 0:
				return temp_c
			elif mode == 1:
				return temp_f
			else:
				return temp_c, temp_f

	def cels(self):
		return self.read_temp(0)

	def fahr(self):
		return self.read_temp(1)
