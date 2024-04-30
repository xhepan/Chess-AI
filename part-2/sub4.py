import chess

def is_consistent_with_window(state, window):
    board = chess.Board(state)

    consistent = True
    window_squares = window.split(";")
    for ws in window_squares:
        square, piece = ws.split(":")
        idx = chess.square(chess.FILE_NAMES.index(square[0]), int(square[1]) - 1)

        if board.piece_at(idx) is None:
            if piece != "?":
                consistent = False
        elif str(board.piece_at(idx)) != piece:
            consistent = False

    return consistent


N = int(input())
potential_states = [input().strip() for _ in range(N)]
window = input().strip()

const_states = []
for state in potential_states:
    if is_consistent_with_window(state, window):
        const_states.append(state)

const_states.sort()
for state in const_states:
    print(state)
