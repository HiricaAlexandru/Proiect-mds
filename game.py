import board
import main
import pygame

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
        self.noMoves += 1
        # Afisez in consola configuratia curenta a tablei de joc si cine muta
        if self.turn == self.board.computer_color:
            print("Computer moves")
        else:
            print("Player moves")

        for r in range(main.ROWS):
            for c in range(main.COLUMNS):
                if self.board.board[r][c] == 0:
                    print('#', end=" ")
                elif self.board.board[r][c].color == main.BLACK:
                    print('B', end=" ")
                else:
                    print("W", end=" ")
            print()
        print('\n')

    def update(self):
        # actualizez jocul in interfata grafica
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self, color):
        # initializez iar jocul
        self.selected = None
        self.board = board.Board(color)
        self.turn = main.BLACK
        self.valid_moves = {}

    def reset(self, color):
        # resetez jocul
        self.DrawConsoleBoard()
        self._init(color)

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