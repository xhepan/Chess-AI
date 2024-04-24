import chess

def is_consistent(fen, window):
    board = chess.Board(fen)
    for square_piece in window.split(';'):
        square, piece = square_piece.split(':')
        if piece == '?':
            if board.piece_at(chess.parse_square(square)) is not None:
                return False
        else:
            if str(board.piece_at(chess.parse_square(square))) != piece:
                return False
    return True

def filter_states(states, window):
    return sorted([state for state in states if is_consistent(state, window)])

# Sample Input
states = [
    "1k6/1ppn4/8/8/8/1P1P4/PN3P2/2K5 w - - 0 32",
    "1k6/1ppnP3/8/8/8/1P1P4/PN3P2/2K5 w - - 0 32",
    "1k6/1ppn1p2/8/8/8/1P1P4/PN3P2/2K5 w - - 0 32"
]
window = "c8:?;d8:?;e8:?;c7:p;d7:n;e7:?;c6:?;d6:?;e6:?"

# Output the list of potential states that are consistent with the window observation
print(filter_states(states, window)[0])
print(filter_states(states, window)[1])