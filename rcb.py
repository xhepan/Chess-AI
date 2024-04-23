import random
import chess.engine
from reconchess import *

class QB(Player):
    def __init__(self):
        self.board = chess.Board()
        self.color = None
        self.my_piece_captured_square = None

        # Stockfish chess engine
        self.engine = chess.engine.SimpleEngine.popen_uci('./stockfish/stockfish-windows-x86-64-avx2.exe')

    def handle_game_start(self, color: Color, board: chess.Board, opponent_name: str):
        self.color = color
        self.board = board

    def handle_opponent_move_result(self, captured_my_piece: bool, capture_square: Optional[Square]):
        self.my_piece_captured_square = capture_square if captured_my_piece else None

    def choose_sense(self, sense_actions: List[Square], move_actions: List[chess.Move], seconds_left: float) -> \
    Tuple[Square, Optional[chess.Move]]:
        # Choose a random square to sense
        sense = random.choice(sense_actions)
        return sense, None

    def handle_sense_result(self, sense_result: List[Tuple[Square, Optional[chess.Piece]]]):
        for square, piece in sense_result:
            self.board.set_piece_at(square, piece)

    def choose_move(self, move_actions: List[chess.Move], seconds_left: float) -> Optional[chess.Move]:
        if len(move_actions) == 0:
            return None

        # Use Stockfish to choose a move
        result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
        return result.move

    def handle_move_result(self, requested_move: Optional[chess.Move], taken_move: Optional[chess.Move],
                       captured_opponent_piece: bool, capture_square: Optional[Square]):
        if requested_move is not None and taken_move is not None:
            self.board.push(taken_move)

    def handle_game_end(self, winner_color: Optional[Color], win_reason: Optional[WinReason],
                        game_history: GameHistory):
        self.engine.quit()
    

# if __name__ == '__main__':
#     reconchess.play_local_game(QB())