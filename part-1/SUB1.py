import chess

def fen_to_ascii(fen):
    board = chess.Board(fen)
    ascii_board = str(board)
    ascii_board = ascii_board.replace('1', '.').replace('2', '..').replace('3', '...').replace('4', '....')
    ascii_board = ascii_board.replace('5', '.....').replace('6', '......').replace('7', '.......').replace('8', '........')
    ascii_board = ascii_board.replace('/', '\n')
    return ascii_board

# Sample Input
fen_input = input()

# Convert FEN to ASCII
ascii_output = fen_to_ascii(fen_input)

# Print ASCII representation of the board
print(ascii_output)
