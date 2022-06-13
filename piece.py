import pygame
import main


class Piece:
    PADDING = 15
    BORDER = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_position()

    def calc_position(self):
        """
        Calculez pozitia pe tabla a unei piese in functie de linia si coloana sa si de dimensiunea unei patratele
        """
        self.x = main.SQUARE_SIZE * self.col + main.SQUARE_SIZE // 2
        self.y = main.SQUARE_SIZE * self.row + main.SQUARE_SIZE // 2

    def make_king(self):
        #Fac o piesa sa fie dama prins schimbarea atributului king
        self.king = True

    def draw(self, window):
        #o piesa considerata rege va avea un alb rosu pe ea
        radius = main.SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(window, main.WHITE, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        if self.king:
            pygame.draw.circle(window, main.WHITE, (self.x, self.y), radius // 3)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_position()

    def __repr__(self):
        return str(self.color)