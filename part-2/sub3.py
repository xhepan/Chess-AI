import chess
import reconchess.utilities as rutils

def generate_next_moves(fen):
    board = chess.Board(fen)
    next_moves = []

    legal_moves = board.legal_moves
    for move in legal_moves:
        next_moves.append(move.uci())

    pseudo_moves = board.pseudo_legal_moves
    for move in pseudo_moves:
        next_moves.append(move.uci())

    # add null move (0000)
    next_moves.append(chess.Move.null().uci())

    for move in rutils.without_opponent_pieces(board).generate_castling_moves():
        if not rutils.is_illegal_castle(board, move):
            next_moves.append(move.uci())

    # remove dups and sort
    unique_moves = list(set(next_moves))
    unique_moves.sort()

    return unique_moves


def generate_next_positions(fen, moves):
    board = chess.Board(fen)
    next_positions = []

    for mov in moves:
        board.push(chess.Move.from_uci(mov))        # make move
        next_positions.append(board.fen())      # get position state
        board.pop()     # unmake move
    
    # sort
    next_positions.sort()
    return next_positions

def generate_next_states(fen, cap_pos):
    board = chess.Board(fen)

    cap_square = chess.square(chess.FILE_NAMES.index(cap_pos[0]), int(cap_pos[1]) - 1)

    moves = generate_next_moves(fen) 

    # check if it's a capturing move
    capturing_moves = []
    for mov in moves:
        move = chess.Move.from_uci(mov)
        if board.is_capture(move) and move.to_square == cap_square:
            capturing_moves.append(move.uci())

    next_states = generate_next_positions(fen, capturing_moves)

    # sort
    next_states.sort()

    return next_states


fen = input()
capture_pos = input()

next_states = generate_next_states(fen, capture_pos)

for state in next_states:
    print(state)
