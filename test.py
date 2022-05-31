import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

electroiman = 21
GPIO.setup(electroiman, GPIO.OUT)
GPIO.output(electroiman, 1)

print("OK")


desp = 240
miniDesp = 120
mov = []
mov.append(posActual[0] - posObj[0])
mov.append(posActual[1] - posObj[1])

if mov[0] > 0: 
	sM1 = 0
else: 
	sM1 = 1

if mov[1] > 0:
	sM2 = 0
else: 
	sM2 = 1

iMax = mov.index(max(mov))

config = []

if mov == [0, 1]:    config.append({0: [1, 0, desp * 1]})
elif mov == [0, -1]: config.append({0: [1, 1, desp * 1]})
elif mov == [1, 0]:  config.append({0: [0, 0, desp * 1]})
elif mov == [-1, 0]: config.append({0: [0, 1, desp * 1]})

mov[0] -= 1
mov[1] -= 1
config.append({0: [0, sM1, miniDesp]})
config.append({1: [1, sM2, (desp * mov[1]) + miniDesp]})
config.append({2: [0, sM1, (desp * mov[0]) + miniDesp]})
config.append({3: [1, sM2, miniDesp]})

for x in range(len(config)):
	m = config[x][0]
	s = config[x][1]
	d = config[x][2]

	for i in range(d):
		for halfstep in range(8):
			for pin in range(4):
				GPIO.output(motores[m[s]], seq[halfstep][pin])
			time.sleep(0.0009)
