import sys
import time
import button
import pygame
import game as gme
import grupButoane as GB
import algorithms as alg
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

bg = pygame.image.load("splash_screen.jpg")
WINDOW.blit(bg, (0,0))

noMoves = 0


############# ecran initial ########################
def deseneaza_alegeri(display, tabla_curenta):

    font = pygame.font.Font(None, 40)
    
    game_name = font.render("Mioveni : Dame",
                                True, (255,255,255))

    display.blit(game_name, (210,30))

    algorithm_choice = font.render("Choose algorithm",
                                True, (255,255,255))
    
    display.blit(algorithm_choice, (360,200))

    choose_side = font.render("Choose side",
                                True, (255,255,255))

    display.blit(choose_side,(30,190))

    difficulty = font.render("Choose difficulty",
                                True, (255,255,255))

    display.blit(difficulty,(30,280))

    game_mode = font.render("Choose game-mode",
                                True, (255,255,255))

    display.blit(game_mode,(30,360))

    btn_alg = GB.GrupButoane(
        top=250,
        left=380,
        listaButoane=[
            button.Button(display=display, w=80, h=30, text="MINIMAX", valoare="minimax"),
            button.Button(display=display, w=120, h=30, text="ALPHABETA", valoare="alphabeta"),
        ],
        indiceSelectat=0,
    )
    btn_juc = GB.GrupButoane(
        top=220,
        left=30,
        listaButoane=[
            button.Button(display=display, w=80, h=30, text="BLACK", valoare="BLACK"),
            button.Button(display=display, w=80, h=30, text="RED", valoare="RED"),
        ],
        indiceSelectat=1,
    )
    btn_dificultate = GB.GrupButoane(
        top=320,
        left=30,
        listaButoane=[
            button.Button(display=display, w=180, h=30, text="BEGINNER", valoare="2"),
            button.Button(display=display, w=180, h=30, text="INTERMEDIATE", valoare="4"),
        ],
        indiceSelectat=0,
    )

    btn_tip_joc = GB.GrupButoane(
        top=390,
        left=30,
        listaButoane=[
            button.Button(display=display, w=180, h=30, text="User vs AI", valoare="cp"),
            button.Button(display=display, w=180, h=30, text="User vs User", valoare="pp"),
            button.Button(display=display, w=180, h=30, text="AI vs AI", valoare="cc"),
        ],
        indiceSelectat=0,
    )

    start = button.Button(
        display=display,
        top=470,
        left=0,
        w=600,
        h=30,
        text="start",
        culoareFundal=RED,
    )
    btn_dificultate.deseneaza()
    btn_alg.deseneaza()
    btn_juc.deseneaza()
    btn_tip_joc.deseneaza()
    start.deseneaza()
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if not btn_alg.selecteazaDupacoord(pos):
                    if not btn_juc.selecteazaDupacoord(pos):
                        if not btn_dificultate.selecteazaDupacoord(pos):
                            if not btn_tip_joc.selecteazaDupacoord(pos):
                                if start.selecteazaDupacoord(pos):
                                    tabla_curenta.reset(btn_juc.getValoare())
                                    return btn_juc.getValoare(), btn_alg.getValoare(), btn_dificultate.getValoare(), btn_tip_joc.getValoare()
        pygame.display.update()


def get_with_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    return row, col

class SesiuneJoc():
    __instance__=None

    def __init__(self):

        if SesiuneJoc.__instance__ is None:
            SesiuneJoc.__instance__ = self
        else:
            raise Exception("O sesiune poate fi accesata doar de catre un utilizator!")

    @staticmethod
    def get_instance():
        # We define the static method to fetch instance
        if not SesiuneJoc.__instance__:
            SesiuneJoc()
        return SesiuneJoc.__instance__


    def start_joc(self):
        pygame.init()
        run = True
        game = gme.Game(WINDOW, "CREAM")
        color, algorithm, depth, game_type = deseneaza_alegeri(WINDOW, game)
        pygame.mixer.music.load('muzica_populara.wav')
        pygame.mixer.music.play(-1)


        if color == "BLACK":
            user_color = BLACK
            computer_color = RED
        else:
            user_color = RED
            computer_color = BLACK
        #am jocul computer vs player
        if game_type == "cp":
            initial_time_game = int(round(time.time() * 1000))
            #initializez pentru a putea afisa la final statisticile
            min_nodes = float('inf')
            max_nodes = float('-inf')
            media_nodes = 0
            min_time = float('inf')
            max_time = float('-inf')
            media_time = 0
            nr_runde = 0

            while run:
                #Verific daca mai am mutari posibile pentru culoarea curenta
                #Daca culoarea curenta s-a blocat atunci opresc jocul
                moreMoves = len(alg.GetAllMoves(game.board, game.turn, game))
                if moreMoves == 0:
                    if game.turn == computer_color:
                        print("Computerul nu mai are mutari. A castigat playerul")
                    else:
                        print("Playerul nu mai are mutari. A castigat computerul")
                    run = False

                if game.turn == computer_color and moreMoves != 0:
                    t_inainte = int(round(time.time() * 1000))
                    if algorithm == "alphabeta":
                        value, new_board, nodes = alg.AlphaBeta(float("-inf"), float("inf"), game.getBoard(), int(depth), computer_color, game, 0)
                        game.computerMove(new_board)
                    else:
                        value, new_board, nodes = alg.MiniMax(game.getBoard(), int(depth), computer_color, game, 0)
                        game.computerMove(new_board)

                    t_dupa = int(round(time.time() * 1000))
                    print(
                        'Calculatorul a "gandit" timp de '
                        + str(t_dupa - t_inainte)
                        + " milisecunde."
                    )
                    nr_runde += 1

                    print("Numarul de noduri: ", nodes)
                    if nodes < min_nodes:
                        min_nodes = nodes
                    elif nodes > max_nodes:
                        max_nodes = nodes
                    media_nodes += nodes

                    media_time += (t_dupa - t_inainte)
                    if t_dupa - t_inainte > max_time:
                        max_time = t_dupa - t_inainte
                    elif t_dupa - t_inainte < min_time:
                        min_time = t_dupa - t_inainte

                if game.winner() != None:
                    if game.winner() == game.getBoard().computer_color:
                        print("Computer won")
                    else: print("Player won")
                    run = False

                if game.turn == user_color and moreMoves != 0:
                    t_inainte = int(round(time.time() * 1000))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            row, col = get_with_mouse(pos)
                            game.select(row, col)
                            t_dupa = int(round(time.time() * 1000))
                            if t_dupa - t_inainte != 0:
                                print(
                                    'Player-ul a "gandit" timp de '
                                    + str(t_dupa - t_inainte)
                                    + " milisecunde."
                                )

                game.update()
            print("\nStatistici pentru calculator")
            print("Timpul minim al calculatorului: " + str(min_time) + " milisecunde" )
            print("Timpul maxim al calculatorului: " +  str(max_time) + " milisecunde")
            print("Media de timp: " + str(media_time / nr_runde) + " milisecunde" )
            print("Numarul minim de noduri: ", min_nodes)
            print("Numarul maxim de noduri: ", max_nodes)
            print("Media de noduri: ", media_nodes / nr_runde)
            final_time_game = int(round(time.time() * 1000))
            print("\nTimpul total de joc:", final_time_game - initial_time_game, "milisecunde")
            print("Numar total de mutari: ", game.noMoves)
            pygame.quit()
        #am jocul player vs player
        elif game_type == "pp":
            while run:

                if game.winner() != None:
                    if game.winner() == game.getBoard().computer_color:
                        print("Computer won")
                    else:
                        print("Player won")
                    run = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        row, col = get_with_mouse(pos)
                        game.select(row, col)
                game.update()
            pygame.quit()
        #am jocul computer vs computer
        else:
            noOfNodes = 0
            while run:
                time.sleep(1)
                if game.winner() != None:
                    if game.winner() == game.getBoard().computer_color:
                        print("Computer won")
                    else:
                        print("Player won")
                    run = False

                if game.turn == computer_color:
                    if algorithm == "alphabeta":
                        value, new_board, noOfNodes = alg.AlphaBeta(-500, 500, game.getBoard(), int(depth), computer_color, game, noOfNodes)
                        game.computerMove(new_board)
                    else:
                        value, new_board, noOfNodes = alg.MiniMax(game.getBoard(), int(depth), computer_color, game, noOfNodes)
                        game.computerMove(new_board)
                else:
                    if algorithm == "alphabeta":
                        value, new_board, noOfNodes = alg.AlphaBeta(-500, 500, game.getBoard(), int(depth), user_color, game, noOfNodes)
                        game.computerMove(new_board)
                    else:
                        value, new_board, noOfNodes = alg.MiniMax(game.getBoard(), int(depth), user_color, game, noOfNodes)
                        game.computerMove(new_board)

                game.update()

            pygame.quit()

joc=SesiuneJoc()
joc.start_joc()

