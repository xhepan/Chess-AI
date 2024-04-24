import chess

def execute_move(fen, move_str):
    board = chess.Board(fen)
    move = chess.Move.from_uci(move_str)
    board.push(move)
    return board.fen()

if __name__ == "__main__":
    fen_input = input().strip()
    move_input = input().strip()
    new_fen = execute_move(fen_input, move_input)
    print(new_fen)
