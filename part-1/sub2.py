import chess

def execute_move(fen, move_str):
    board = chess.Board(fen)
    move = chess.Move.from_uci(move_str)
    board.push(move)  # Make the move

    return board.fen()


# Sample Input
fen_input = input()
move_string = input()

output_string = execute_move(fen_input, move_string)

print(output_string)

