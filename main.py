from juego import *
from vision import *
from electronica import *
from funcionesAux import *


#Inicializamos las matrices de los tableros
tablero_aux, tablero_A, tablero_S = initTaulers()

#Inicializamos el tablero que utilitza la lib chess y cargamos Stockfish en el engine
board, engine = initJuego()

#Cargamos los modelos
modelo_T, modelo_P = initModels()

while board.is_checkmate() == False:

    turno = 'P'

    deteccionTablero(modelo_T)
    casillas = './Casillas'
    aplicarModelo(modelo_P, casillas, tablero_A, 'P')
    time.sleep(5)

    deteccionTablero(modelo_T)
    casillas = './Casillas'
    aplicarModelo(modelo_P, casillas, tablero_S, 'P')

    dif = np.subtract(tablero_S, tablero_A)
    jugada = traducirJugadaPlayer(dif, tablero_aux)

    jugadaP = makePlay(board, None, jugada, turno)

    if jugadaP == False:
        print("Movimiento no permitido")
        print("Deshaga el movimiento y haga otro")
        time.sleep(10)
        continue

    turno = 'IA'

    jugadaIA = makePlay(board, engine, None, turno)
    traducirJugadaIA()

    controlMotores()
    electroiman(1)
    
    controlMotores()
    electroiman(0)