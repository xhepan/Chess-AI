import chess
import reconchess

def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def get_possible_positions(fen):
    board = chess.Board(fen)
    moves = list(board.legal_moves)
    pseudolegal_moves = list(board.pseudo_legal_moves)
    moves.append(chess.Move.null())
    moves = moves + pseudolegal_moves
    for move in reconchess.utilities.without_opponent_pieces(board).generate_castling_moves():
        if not reconchess.utilities.is_illegal_castle(board, move):
            moves.append(move)
    moves = remove_duplicates(moves)
    moves = sorted(map(str, moves))
    positions = []
    for move in moves:
        board.push(chess.Move.from_uci(move))
        positions.append(board.fen())
        board.pop()

    positions.sort()
    for position in positions:
        print(position)



if __name__ == "__main__":
    fen_input = input().strip()
    get_possible_positions(fen_input)
