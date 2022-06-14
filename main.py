import sys
import time
import button
import pygame
from copy import deepcopy

# setez valorile pentru numarul de coloane, randuri, inaltimea si latimea tablei de joc
WIDTH, HEIGHT = 600, 600
ROWS, COLUMNS = 8, 8
SQUARE_SIZE = WIDTH // COLUMNS

# setez valorile pentru culorile pe care le folosesc
RED = (255, 0, 0)       #pentru a ilustra o piesa rege
CREAM = (248, 226, 177)     #piesa si patratel
BLACK = (0, 0, 0)       #piesa si patratel
WHITE = (255, 255, 255)      #pentru a ilustra user ului posibilele mutari     #pentru a putea distinge piesele negre pe patratele negre


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mioveni : Dame')
noMoves = 0

