import board
import pygame

# setez valorile pentru culorile pe care le folosesc
RED = (255, 0, 0)       #pentru a ilustra o piesa rege
CREAM = (248, 226, 177)     #piesa si patratel
BLACK = (0, 0, 0)       #piesa si patratel
WHITE = (255, 255, 255)      #pentru a ilustra user ului posibilele mutari     #pentru a putea distinge piesele negre pe patratele negre

WIDTH, HEIGHT = 600, 600
ROWS, COLUMNS = 8, 8
SQUARE_SIZE = WIDTH // COLUMNS


class Game:
    #Clasa care se ocupa de gestionarea jocului
    def __init__(self, window, user_color):
        self.selected = None
        self.board = board.Board(user_color)
        self.turn = BLACK       #negrul muta primul asa ca initializez jocul cu negru
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

        for r in range(ROWS):
            for c in range(COLUMNS):
                if self.board.board[r][c] == 0:
                    print('#', end=" ")
                elif self.board.board[r][c].color == BLACK:
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
        self.turn = BLACK
        self.valid_moves = {}

    def reset(self, color):
        # resetez jocul
        self.DrawConsoleBoard()
        self._init(color)

    def select(self, row, col):

        """
        :param row: linia de pe care vreau sa selectez o piesa
        :param col: coloana de pe care vreau sa selectez piesa
        :return: True daca s-a putut face selectia, False altfel
        """
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)

            return True
        return False

    def _move(self, row, col):
        """
        :param row: linia pe care doresc sa mut
        :param col: coloana pe care doresc sa mut
        Verific daca mutarea pe care vreau sa o fac este valida
        Daca dupa efectuarea mutarii am sarit peste piese ale adversarului atunci le sterg de pe tabla
        Schimb randul (daca tocmai a mutat rosu atunci va fi randul lui negru si invers)
        """
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()

        else:
            return False
        return True

    def change_turn(self):
        # Daca tocmai a mutat rosu atunci va fi randul lui negru si invers
        self.valid_moves = {}
        if self.turn == self.board.user_color:
            self.turn = self.board.computer_color
        else:
            self.turn = self.board.user_color
        self.DrawConsoleBoard()

    def draw_valid_moves(self, moves):
        """
        :param moves: Mutarile valide pentru piesa selectata
        Ii afisez utilizatorului unde se poate misca piesa pe care a selectat-o
        """
        for move in moves:
            row, col = move
            pygame.draw.circle(self.window, WHITE,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                row * SQUARE_SIZE + SQUARE_SIZE // 2),
                               15)

    def winner(self):
        """
        :return: cine a castigat (alb sau negru)
        """
        return self.board.winner()

    def getBoard(self):
        """
        :return: configuratia actuala a tablei de joc
        """
        return self.board

    def computerMove(self, board):
        """
        :param board: configuratia actuala a tablei
        Schimb randul dupa ce a mutat calculatorul
        """
        self.board = board
        self.change_turn()


