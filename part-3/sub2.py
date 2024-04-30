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


def most_common_move(moves):
    move_occur = {}
    for move in moves:
        move_occur[move] = move_occur.get(move, 0) + 1
    
    max_num_occur = max(move_occur.values())

    most_common_moves = []
    for move, count in move_occur.items():
        if count == max_num_occur:
            most_common_moves.append(move)

    return sorted(most_common_moves)[0]




N = int(input().strip())
fen_list = [input().strip() for _ in range(N)]

moves = []
for fen in fen_list:
    next_move = generate_move(fen)
    moves.append(next_move)


print(most_common_move(moves))
