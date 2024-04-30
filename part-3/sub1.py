import chess
import chess.engine

def generate_move(fen):
    board = chess.Board(fen)

    # check if checkmate (to opponent)
    if board.is_checkmate():
        for move in board.legal_moves:
            if move.to_square == board.king(not board.turn):
                return move.uci()

    # stockfish move
    with chess.engine.SimpleEngine.popen_uci('./stockfish', setpgrp=True) as engine:
        result = engine.play(board, chess.engine.Limit(time=0.5))
        return result.move.uci()



fen = input()

next_move = generate_move(fen)
print(next_move)
