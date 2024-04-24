from collections import Counter
import chess.engine

def get_move_using_stockfish(fen):
    # with chess.engine.SimpleEngine.popen_uci('./stockfish/stockfish-windows-x86-64-avx2.exe', setpgrp=True) as engine:
    with chess.engine.SimpleEngine.popen_uci('/opt/stockfish/stockfish', setpgrp=True) as engine:
        board = chess.Board(fen)
        
        if board.is_check():
            for move in board.legal_moves:
                if board.is_capture(move):
                    return move.uci()

        
        result = engine.play(board, chess.engine.Limit(time=0.5))
        return result.move.uci()
    
def get_most_common_move(fen_list):
    move_counts = Counter()
    for fen in fen_list:
        move = get_move_using_stockfish(fen)
        move_counts[move] += 1

    most_common_moves = move_counts.most_common()
    most_common_move = sorted(most_common_moves, key=lambda x: (-x[1], x[0]))[0][0]
    return most_common_move

if __name__ == "__main__":
    N = int(input())
    fen_list = [input().strip() for _ in range(N)]
    common_move = get_most_common_move(fen_list)
    print(common_move)
