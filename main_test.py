#!/usr/bin/python
# Main Launcher
from __future__ import division
import time, math, sys, os
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)


print 'Initializing motors...'

motor_pins = [11,13,16,22]

GPIO.setup(motor_pins[0], GPIO.OUT)
GPIO.setup(motor_pins[1], GPIO.OUT)
GPIO.setup(motor_pins[2], GPIO.OUT)
GPIO.setup(motor_pins[3], GPIO.OUT)

front_left = GPIO.PWM(motor_pins[0],50)
front_right = GPIO.PWM(motor_pins[1],50)
rear_left = GPIO.PWM(motor_pins[2],50)
rear_right = GPIO.PWM(motor_pins[3],50)

calibr = raw_input('Do you want to calibrate? (y/n)')

if calibr == 'y':
	front_left.start(10)
	front_right.start(10)
	rear_left.start(10)
	rear_right.start(10)
	resp = raw_input('Plug-in power and quickly press enter.')
	front_left.ChangeDutyCycle(5)
	front_right.ChangeDutyCycle(5)
	rear_left.ChangeDutyCycle(5)
	rear_right.ChangeDutyCycle(5)
	print 'Finished calibration?'

else:
	gotit = raw_input('Plug-in power and press enter.')

	print 'Starting stand-by mode...'

	front_left.start(5)
	front_right.start(5)
	rear_left.start(5)
	rear_right.start(5)


print 'Waiting for commands...'
activ = True
while activ == True:
	comnd = raw_input('Enter command (set/stop):')
	if comnd == 'set':
		amnt = float(raw_input('Set Speed (0.0-10.0):'))
		front_left.ChangeDutyCycle(amnt)
		front_right.ChangeDutyCycle(amnt)
		rear_left.ChangeDutyCycle(amnt)
		rear_right.ChangeDutyCycle(amnt)
		print 'Speed is now',amnt
	if comnd == 'stop':
		front_left.ChangeDutyCycle(0)
		front_right.ChangeDutyCycle(0)
		rear_left.ChangeDutyCycle(0)
		rear_right.ChangeDutyCycle(0)
		front_left.stop()
		front_right.stop()
		rear_left.stop()
		rear_right.stop()
		GPIO.cleanup()
		activ = False
		print 'Stopped everything...'



