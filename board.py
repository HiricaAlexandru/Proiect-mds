import pygame
import main
import piece
class Board:

    def __init__(self, color):
        if color == "BLACK":
            self.user_color = main.BLACK
            self.computer_color = main.RED
        else:
            self.user_color = main.RED
            self.computer_color = main.BLACK
        self.board = []
        # cate piese mai are fiecare jucator
        self.black_left = self.red_left = 12
        self.black_kings = self.red_kings = 0
        self.create_board()

    # tabla initiala
    def draw_squares(self, window):
        """
        :param window: fereastra unde voi desena
        Desenez patratelele pe care vor fi pozitionate piesele de joc
        """
        # initial voi avea toate patratele negre
        window.fill(main.BLACK)
        # alternez patrate rosi cu patrate negre
        for row in range(main.ROWS):
            for col in range(row % 2, main.COLUMNS, 2):
                pygame.draw.rect(window, main.CREAM, (row * main.SQUARE_SIZE, col * main.SQUARE_SIZE, main.SQUARE_SIZE, main.SQUARE_SIZE))

    def move(self, piece, row, col):
        """
        :param piece: piesa pe care vreau sa o mut
        :param row: linia pe care vreau sa o mut
        :param col: coloana pe care vreau sa o mut
        Verific daca piesa pe care am ajuns sa o mut a ajuns la stadiu de pisa rege sau nu
        """
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == main.ROWS - 1 or row == 0:
            if piece.king is False:
                piece.make_king()
                if piece.color == main.RED:
                    self.red_kings += 1
                else:
                    self.black_kings += 1

    def get_piece(self, row, col):
        """
        :param row: linia pe care se afla piesa
        :param col: coloana pe care se afla piesa
        :return: piesa de la linia si coloana date ca parametru
        """
        return self.board[row][col]

    def create_board(self):
        """
        Creez tabla de joc initiala cu toate piesele in pozitiile initiale
        """
        for row in range(main.ROWS):
            self.board.append([])
            for col in range(main.COLUMNS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(piece.Piece(row, col, self.computer_color))
                    elif row > 4:
                        self.board[row].append(piece.Piece(row, col, self.user_color))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, window):
        """
        :param window: fereastra unde desenez
        Desenez fereastra si piesele
        """
        self.draw_squares(window)
        for row in range(main.ROWS):
            for col in range(main.COLUMNS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)