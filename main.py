#!/usr/bin/python
# Main Launcher
from __future__ import division
import time, math, sys, os
import RPi.GPIO as GPIO

from Motor import Motor
from DS18B10 import Temperature
from MPU6050 import Gyro
#from GPS6MV import GPS
#from QC1602A import LCD
#from Camera import Camera

GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)


print 'Initializing sensors and misc boards...'

temperature = Temperature()
gyro = Gyro(1)
#gps = GPS()
#lcd = LCD()
#camera = Camera()

print 'Initializing motors...'

motor_pins = [11,13,15,16]

front_left = Motor(motor_pins[0],GPIO)
front_right = Motor(motor_pins[1],GPIO)
rear_left = Motor(motor_pins[2],GPIO)
rear_right = Motor(motor_pins[3],GPIO)


print 'Starting stand-by mode...'

front_left.start()
front_right.start()
rear_left.start()
rear_right.start()

# Wait 2 seconds, to let motors finish initialization
time.sleep(2);


print 'Waiting for commands...'

# THIS IS GOING TO CHANGE SOON!
while True:
	command = raw_input('Enter command: ')

	if command == 'increase front':
		front_left.set_speed('increase')
		front_right.set_speed('increase')

	elif command == 'increase back':
		rear_left.set_speed('increase')
		rear_right.set_speed('increase')

	elif command == 'speed 50':
		front_left.set_speed(50)
		front_right.set_speed(50)
		rear_left.set_speed(50)
		rear_right.set_speed(0)



