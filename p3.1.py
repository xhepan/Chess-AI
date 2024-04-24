import chess.engine

def get_move_using_stockfish(fen):
    with chess.engine.SimpleEngine.popen_uci('/opt/stockfish/stockfish', setpgrp=True) as engine:
        board = chess.Board(fen)
        
        if board.is_check():
            for move in board.legal_moves:
                if board.is_capture(move):
                    return move.uci()

        
        result = engine.play(board, chess.engine.Limit(time=0.5))
        return result.move.uci()

if __name__ == "__main__":
    fen_input = input().strip()
    move = get_move_using_stockfish(fen_input)
    print(move)
