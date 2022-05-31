import time
import RPi.GPIO as GPIO

def initElectronica():
	GPIO.setmode(GPIO.BCM)

	pins_M1 = [[17,18,27,22], [22,27,18,17]]
	pins_M2 = [[23,24,25,8], [8,25,24,23]]
	lista_pins = [pins_M1, pins_M2]

	for M1, M2 in zip(pins_M1[0], pins_M2[0]):
		GPIO.setup(M1, GPIO.OUT)
		GPIO.setup(M2, GPIO.OUT)
		GPIO.output(M1, 0)
		GPIO.output(M2, 0)

	electroiman = 21
	GPIO.setup(electroiman, GPIO.OUT)		

	sequencia_M =  [[1,0,0,0],
					[1,1,0,0],
					[0,1,0,0],
					[0,1,1,0],
					[0,0,1,0],
					[0,0,1,1],
					[0,0,0,1],
					[1,0,0,1]]

	return lista_pins, electroiman, sequencia_M


def controlMotores(motores, posActual, posObj, seq):
	desp = 600
	miniDesp = 300
	mov = []
	mov.append(posActual[0] - posObj[0])
	mov.append(posActual[1] - posObj[1])

	if mov[0] > 0: 
		sM1 = 1
	else: 
		sM1 = 0

	if mov[1] > 0:
		sM2 = 1
	else: 
		sM2 = 0

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



def activaElectroiman(electroiman, pulso):
	GPIO.output(electroiman, pulso)
