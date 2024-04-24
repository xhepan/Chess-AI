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

if __name__ == "__main__":
    N = int(input())
    potential_states = [input().strip() for _ in range(N)]
    window = input().strip()

    consistent_states = filter_states(potential_states,window)
    for state in consistent_states:
        print(state)
