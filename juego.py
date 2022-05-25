import chess
import chess.engine


def initJuego():
    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci(r"Recursos/Stockfish.exe")
    return board, engine


def makePlay(board, engine, jugada, player):
    if player == 'P':
        movimiento = chess.Move.from_uci(jugada)
        if movimiento not in board.legal_moves:
            return False
        else:
            board.push(movimiento)
            return True

    elif player == 'IA':
        result = engine.play(board, chess.engine.Limit(time = 0.1))
        print("Movimiento StockFish:" + str(result.move))
        board.push(result.move)

        return str(result.move)