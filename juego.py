import chess
import chess.engine


def initJuego():
    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci("Stockfish/src/stockfish")
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

        mI = result.move.from_square
        mF = result.move.to_square

        return mI, mF 
