import numpy as np

class Casilla:
    def __init__(self, l, n):
        self.pos = l + str(n)


def initTaulers():
    tablero_1 = np.zeros((8, 8), dtype=int)
    tablero_2 = np.zeros((8, 8), dtype=int)
    tablero_aux = np.zeros((8, 8), dtype=Casilla)

    letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i, letra in zip(range(8), letras):
        for j in range(8):
            tablero_aux[j][i] = Casilla(letra, 8 - j)

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


def traducirJugadaIA():
    a = 0