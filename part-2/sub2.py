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


fen = input()

moves = generate_next_moves(fen)
next_positions = generate_next_positions(fen, moves)
for position in next_positions:
    print(position)
