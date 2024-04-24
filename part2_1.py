import chess


def generate_moves(fen):
    board = chess.Board(fen)
    legal_moves = []

    # Add null move (0000)
    legal_moves.append("0000")

    # Generate other legal moves
    for move in board.legal_moves:
        legal_moves.append(move.uci())

    legal_moves.sort()
    return legal_moves


# Sample Input
fen_input = input()

# Generate legal moves
next_moves = generate_moves(fen_input)

# Print the next possible moves
print()
for move in next_moves:
    print(move)
