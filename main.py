from juego import *
from vision import *
from electronica import *
from funcionesAux import *

#Inicializamos las matrices de los tableros
tablero_aux, tablero_A, tablero_S = initTaulers()
print("Tableros inicializados")

#Inicializamos el tablero que utilitza la lib chess y cargamos Stockfish en el engine
board, engine = initJuego()
print("Entorno de juego creado")

#Cargamos los modelos
modelo_T, modelo_P = initModels()
print("Modelos cargados")

#Inicializamos los pines de los componentes de HW
pins_motores, electroiman, seq_motores = initElectronica()
print("Hardware configurado \n")

posAct = [1, 1]

print("Estado actual tablero: ")
print(board)

check = input()

while board.is_checkmate() == False:
    turno = 'P'
    jugadaP = False
    iguales = True

    deteccionTablero(modelo_T)
    casillas = './Casillas'
    aplicarModelo(modelo_P, casillas, tablero_A, 'P')
    time.sleep(5)

    print("Primera captura")
    print(tablero_A, "\n")

    while jugadaP == False:
        deteccionTablero(modelo_T)
        casillas = './Casillas'
        aplicarModelo(modelo_P, casillas, tablero_S, 'P')
        
        
        if not np.array_equal(tablero_A, tablero_S):
            iguales = False
            print("Segunda captura")
            print(tablero_S, "\n")
        else:
            'No se ha realizado ningún movimiento'

        if iguales == False:
            dif = np.subtract(tablero_S, tablero_A)
            jugada = traducirJugadaPlayer(dif, tablero_aux)

            jugadaP = makePlay(board, None, jugada, turno)

            if jugadaP == False:
                print("Movimiento no permitido")
                print("Deshaga el movimiento y realice otro distinto")
                time.sleep(10)
            else:
                print("Jugada correcta, turno IA \n")

    turno = 'IA'

    mI, mF = makePlay(board, engine, None, turno)
    print("Estado actual tablero: ")
    print(board)
    check = input()
    
    posInicio, posFinal = traducirJugadaIA(mI, mF, tablero_aux)

    print("Control motores 1")
    controlMotores(pins_motores, posAct, posInicio, seq_motores)
    electroiman(1)
    
    print("Control motores 2")
    controlMotores(pins_motores, posInicio, posFinal, seq_motores)
    electroiman(0)
    
    print("Estado actual tablero: ")
    print(board)
    check = input()

    posAct = posFinal

GPIO.cleanup()
