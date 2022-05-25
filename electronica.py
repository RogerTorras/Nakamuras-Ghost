import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

control_pins_m1 = [17,18,27,22]
control_pins_m2 = [17,18,27,22]
electroiman = True

for pin in control_pins_m1:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)

for pin in control_pins_m2:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)

halfstep_seq = [
	[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1]
]

vueltas = 30
round = 512 * vueltas

for i in range(round):
	for halfstep in range(8):
		for pin in range(4):
			GPIO.output(control_pins_m1[pin],halfstep_seq[halfstep][pin])
		time.sleep(0.0009)

for i in range(round):
	for halfstep in range(8):
		for pin in range(4):
			GPIO.output(control_pins_m2[pin],halfstep_seq[halfstep][pin])
		time.sleep(0.0009)

GPIO.cleanup()

def controlMotores():
	a = 0

def electroiman(activa):
	GPIO.setmode(GPIO.BCM)		#Mirarlo

	GPIO.setup(23, GPIO.OUT)
	GPIO.output(23, activa)

	GPIO.cleanup()