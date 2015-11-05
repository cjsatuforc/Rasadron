import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pn = 11 # CHANGE THIS TO YOUR PIN!
fq = 50.0
dc = 0.0

GPIO.setup(pn, GPIO.OUT)
p = GPIO.PWM(pn, fq)
p.start(dc)

time.sleep(2)

activ = True
while activ == True:
	comnd = raw_input('Enter command:')
	if comnd == 'set':
		amnt = float(raw_input('Set Duty Cycle:'))
		dc = amnt
		p.ChangeDutyCycle(dc)
		print 'Duty Cycle is now',dc
	if comnd == 'incr':
		dc = dc+0.1
		p.ChangeDutyCycle(dc)
		print 'Duty Cycle is now',dc
	if comnd == 'decr':
		dc = dc-0.1
		p.ChangeDutyCycle(dc)
		print 'Duty Cycle is now',dc
	if comnd == 'stop':
		activ = False
		p.ChangeDutyCycle(0.0)
		p.stop()
		GPIO.cleanup()
		print 'Stopped. Last Duty Cycle was',dc
