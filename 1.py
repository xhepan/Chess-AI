import chess

def fen_to_board(fen):
    board = chess.Board(fen)
    board_string = str(board)
    board_string = board_string.replace(' ', '')  # Remove spaces for formatting
    return board_string


        
if __name__ == "__main__":
    fen_input = input().strip()
    board_string = fen_to_board(fen_input)
    print(board_string)
