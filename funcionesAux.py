import numpy as np

class Casilla:
    def __init__(self, l, n, v, c):
        self.pos = l + str(n)
        self.value = v
        self.coord = c


def initTaulers():
    tablero_1 = np.zeros((8, 8), dtype=int)
    tablero_2 = np.zeros((8, 8), dtype=int)
    tablero_aux = np.zeros((8, 8), dtype=Casilla)

    letras = ["a", "b", "c", "d", "e", "f", "g", "h"]

    for i, letra in zip(range(8), letras):
        for j in range(8):
            tablero_aux[j][i] = Casilla(letra, 8 - j, -1, [0, 0])

    cnt = 1

    for i in range(8):
        for j in range(8):
            tablero_aux[i][7-j].value = 64 - cnt
            tablero_aux[i][j].coord = [i, j]
            cnt += 1

    return tablero_aux, tablero_1, tablero_2


def traducirJugadaPlayer(resta, tablero_aux):
    posInicial = np.where(resta == -1)
    p0 = int(posInicial[0])
    p1 = int(posInicial[1])
    posInicial = tablero_aux[p0][p1].pos

    posFinal = np.where(resta == 1)
    p0 = int(posFinal[0])
    p1 = int(posFinal[1])
    posFinal = tablero_aux[p0][p1].pos
    
    movimiento = posInicial + posFinal
    return movimiento


def traducirJugadaIA(mI, mF, t):
    posInicio = [casilla.coord for c in t for casilla in c if casilla.value == mI]
    posFinal =  [casilla.coord for c in t for casilla in c if casilla.value == mF]

    return posInicio[0], posFinal[0]