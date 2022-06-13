import board
import main

class Game:
    #Clasa care se ocupa de gestionarea jocului
    def __init__(self, window, user_color):
        self.selected = None
        self.board = board.Board(user_color)
        self.turn = main.BLACK       #negrul muta primul asa ca initializez jocul cu negru
        self.valid_moves = {}
        self.window = window
        self.noMoves = 0

    def DrawConsoleBoard(self):
        pass

    def update(self):
        pass

    def _init(self, color):
        pass

    def reset(self, color):
        pass

    def select(self, row, col):
        pass

    def _move(self, row, col):
        pass

    def change_turn(self):
        pass

    def draw_valid_moves(self, moves):
        pass

    def winner(self):
        pass

    def getBoard(self):
        pass

    def computerMove(self, board):
        pass