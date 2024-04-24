import chess

def generate_next_positions_with_capture(fen, square):
    board = chess.Board(fen)
    next_positions = []

    # Generate all moves that result in a capture on the specified square
    for move in board.legal_moves:
        if move.to_square == chess.parse_square(square) and board.is_capture(move):
            board_copy = board.copy()  # Create a copy of the board
            board_copy.push(move)      # Apply the move to the copy
            next_positions.append(board_copy.fen())  # Append the resulting FEN string to the list

    return sorted(next_positions)

if __name__ == "__main__":
    fen_input = input().strip()
    square = input().strip()
    next_positions = generate_next_positions_with_capture(fen_input, square)
    for position in next_positions:
        print(position)
