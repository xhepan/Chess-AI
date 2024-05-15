from reconchess import *
import chess.engine
import random
import os

class RandomSensing(Player):
    def __init__(self):
        self.board = None           # current state
        self.color = None
        self.stockfish_path = './stockfish'
        self.move = None
        self.opponent_move = None
        self.opponent_moves = []
        # self.opponent_move_history = []
        # self.move_history = []
        self.turn = None
        # self.move_num = 0
        self.states = set()
        self.moves = []

    def handle_game_start(self, color: Color, board: chess.Board, opponent_name: str):
        self.board = board
        self.color = color
        self.turn = color
        # self.move_num = 0
        # self.engine = chess.engine.SimpleEngine.popen_uci(self.stockfish_path, setpgrp=True, timeout=10/10000)
        self.engine = chess.engine.SimpleEngine.popen_uci(self.stockfish_path, setpgrp=True)

        self.moves = list(board.legal_moves)

        next_positions = []
        for move in self.moves:
            board.push(move) 
            next_positions.append(board.fen())  
            board.pop() 
            
            # sort
            next_positions.sort()

        self.states = set(next_positions)
        

    
    def handle_opponent_move_result(self, captured_my_piece: bool, capture_square: Optional[Square]):
        self.my_piece_captured_square = capture_square
        if captured_my_piece:
            self.board.remove_piece_at(capture_square)

        if self.opponent_move is not None:
            self.opponent_moves.append(self.opponent_move)
            # self.opponent_move_history.append(self.opponent_move.uci())

            # Update the list of legal moves
            self.moves = list(self.board.legal_moves)
            # self.moves = self.check_num_moves(moves)

            # Update the list of next positions
            next_positions = []
            for move in self.moves:
                self.board.push(move)
                next_positions.append(self.board.fen())
                self.board.pop()

            # Sort the next positions
            next_positions.sort()

            # Update the set of states
            self.states = set(next_positions)

        # Reset the opponent move
        self.opponent_move = None



    def choose_sense(self, sense_actions: List[Square], move_actions: List[chess.Move], seconds_left: float) -> Square:
        if self.my_piece_captured_square:
            return self.my_piece_captured_square

        def is_edge_square(square: Square) -> bool:
            file, rank = chess.square_file(square), chess.square_rank(square)
            return file == 0 or file == 7 or rank == 0 or rank == 7
        
        sense_actions = [square for square in sense_actions if not is_edge_square(square)]

        return random.choice(sense_actions)
    

    def handle_sense_result(self, sense_result: List[Tuple[Square, Optional[chess.Piece]]]):
        for square, piece in sense_result:
            if piece is not None:
                self.board.set_piece_at(square, piece)
            else:
                self.board.remove_piece_at(square)

        if self.my_piece_captured_square:
            possible_moves = []
            for move in self.moves:
                if move.to_square == self.my_piece_captured_square:
                    possible_moves.append(move)
            self.moves = possible_moves


    def choose_move(self, move_actions, seconds_left: float) -> Optional[chess.Move]:
        next_moves = []
        for move in move_actions:
            next_moves.append(move.uci())

        # remove dups and sort
        unique_moves = list(set(next_moves))
        unique_moves.sort()


        move_occur = {}
        for move in unique_moves:
            move_occur[move] = move_occur.get(move, 0) + 1
        
        max_num_occur = max(move_occur.values())

        most_common_moves = []
        for move, count in move_occur.items():
            if count == max_num_occur:
                most_common_moves.append(move)

        mov = sorted(most_common_moves)[0]
        return chess.Move.from_uci(mov)


    def handle_move_result(self, requested_move: Optional[chess.Move], taken_move: Optional[chess.Move], captured_opponent_piece: bool, capture_square: Optional[Square]):
        if taken_move is not None:
            self.board.push(taken_move)

        # Update the list of legal moves
        self.moves = list(self.board.legal_moves)

        # Update the list of next positions
        next_positions = []
        for move in self.moves:
            self.board.push(move)
            next_positions.append(self.board.fen())
            self.board.pop()

        # Sort the next positions
        next_positions.sort()

        # Update the set of states
        self.states = set(next_positions)


    def handle_game_end(self, winner_color: Optional[Color], win_reason: Optional[WinReason], game_history: GameHistory):
        try:
            self.engine.quit()
        except chess.engine.EngineTerminatedError:
            pass


    def check_num_moves(self, moves):
        if (len(moves) >= 10000):
            num_moves_to_remove = 1000

            # Randomly select moves to remove
            moves_to_remove = random.sample(moves, num_moves_to_remove)

            # Remove selected moves from the list
            for move in moves_to_remove:
                moves.remove(move)

        return moves
