import chess
import reconchess

def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def get_possible_moves():
    # Take FEN string as user input
    fen = input().strip()

    # Create a chess board from the FEN string
    board = chess.Board(fen)

    # Generate all possible moves
    moves = list(board.legal_moves)
    pseudolegal_moves = list(board.pseudo_legal_moves)
    moves.append(chess.Move.null())
    moves = moves + pseudolegal_moves
   

    for move in reconchess.utilities.without_opponent_pieces(board).generate_castling_moves():
        if not reconchess.utilities.is_illegal_castle(board, move):
            moves.append(move)
     
    moves = remove_duplicates(moves)
    # Convert the moves to strings and sort them
    moves = sorted(map(str, moves))

    # Print the possible moves
    for move in moves:
        print(move)

get_possible_moves()
