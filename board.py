import pygame
import piece

# setez valorile pentru culorile pe care le folosesc
RED = (255, 0, 0)       #pentru a ilustra o piesa rege
CREAM = (248, 226, 177)     #piesa si patratel
BLACK = (0, 0, 0)       #piesa si patratel
WHITE = (255, 255, 255)      #pentru a ilustra user ului posibilele mutari     #pentru a putea distinge piesele negre pe patratele negre

WIDTH, HEIGHT = 600, 600
ROWS, COLUMNS = 8, 8
SQUARE_SIZE = WIDTH // COLUMNS


class Board:

    def __init__(self, color):
        if color == "BLACK":
            self.user_color = BLACK
            self.computer_color = RED
        else:
            self.user_color = RED
            self.computer_color = BLACK
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
        window.fill(BLACK)
        # alternez patrate rosi cu patrate negre
        for row in range(ROWS):
            for col in range(row % 2, COLUMNS, 2):
                pygame.draw.rect(window, CREAM, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        """
        :param piece: piesa pe care vreau sa o mut
        :param row: linia pe care vreau sa o mut
        :param col: coloana pe care vreau sa o mut
        Verific daca piesa pe care am ajuns sa o mut a ajuns la stadiu de pisa rege sau nu
        """
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            if piece.king is False:
                piece.make_king()
                if piece.color == RED:
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
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLUMNS):
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
        for row in range(ROWS):
            for col in range(COLUMNS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)


    def winner(self):
        # Daca rosu a ramas fara piese atunci a castigat negru
        # Daca negru a ramas fara piese atunci a castigat rosu
        if self.red_left <= 0:
            return BLACK
        elif self.black_left <= 0:
            return RED
        return None

    def get_valid_moves(self, piece):
        """
        :param piece: piesa pe care vreau sa o mut la un moment
        :return: returneaza un dictionar format din posibilele pozitii unde voi muta piesa
        Piesele rege se pot muta si in sus si in jos, de aceea iau in considerare in ambele cazuri
        Pasul cu care ma mut reprezinta directia (daca in sus sau in jos)
        """
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        if piece.color == self.user_color or piece.king:
            moves.update(self._look_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._look_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == self.computer_color or piece.king:
            moves.update(self._look_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._look_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        return moves

    def _look_left(self, start, stop, step, color, left, skipped=[]):
        """
        :param start: locul de unde pornesc
        :param stop: locul unde ma opresc
        :param step: pasul cu care merg (in sus sau in jos)
        :param color: culoarea care muta acum
        :param left: directia in care caut (stanga sau dreapta)
        :param skipped: lista ce contine piesele peste care am sarit
        :return: dictionar ce contine locurile unde pot muta piesa selectata inspre stanga
        Cheia dictionarului va fi pozitia la care vreau sa ma mut formata din tuplu (linie, coloana)
        Fiecare pozitie ce reprezinta o cheie contine un dictionar care contine pozitiile unde pot ajunge de acolo
        (Daca sar peste o piesa vreau sa vad daca mai am cum sa sar)
        (Daca am doar loc liber in casuta respectiva atunci nu mai pot sari mai departe)
        (Verific doar pentru maxim 3 randuri mai departe adica verific daca am saritura dubla)
        """
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._look_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._look_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _look_right(self, start, stop, step, color, right, skipped=[]):
        """
        :param start: locul de unde pornesc
        :param stop: locul unde ma opresc
        :param step: pasul cu care merg
        :param color: culoarea care muta acum
        :param right: directia in care caut
        :param skipped: lista ce contine piesele peste care am sarit
        :return: dictionar ce contine locurile unde pot muta piesa selectata inspre dreapta
        Cheia dictionarului va fi pozitia la care vreau sa ma mut formata din tuplu (linie, coloana)
        Fiecare pozitie ce reprezinta o cheie contine un dictionar care contine pozitiile unde pot ajunge de acolo
        (Daca sar peste o piesa vreau sa vad daca mai am cum sa sar)
        (Daca am doar loc liber in casuta respectiva atunci nu mai pot sari mai departe)
        (Verific doar pentru maxim 3 randuri mai departe adica verific daca am saritura dubla)
        """
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLUMNS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._look_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._look_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves

    def remove(self, pieces):
        #Sterg o piesa de pe tabla
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.black_left -= 1


    #Estimari ale scorului
    def evaluateScore1(self):
            #diferenta de peise, tinand cont de numarul de dame
        if self.computer_color == BLACK:
            return self.black_left - self.red_left + (self.black_kings * 0.5 - self.red_kings * 0.5)
        else:
            return self.red_left - self.black_left + (self.red_kings * 0.5 - self.black_kings * 0.5)

    def evaluateScore2(self):
        # diferenta de peise far aa tine cont de numarul de dame
        if self.computer_color == BLACK:
            return self.black_left - self.red_left
        else:
            return self.red_left - self.black_left

    def getAllPieces(self, color):
        """
        :param color: culoarea dorita (rosu sau negru)
        :return: o lista formata din toate piesele de culoarea data ca parametru
        """
        pieces = []
        for r in self.board:
            for p in r:
                if p != 0 and p.color == color:
                    pieces.append(p)
        return pieces
