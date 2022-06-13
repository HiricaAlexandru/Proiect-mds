from copy import deepcopy

def SimulateMove(piece, move, board, game, skip):
    """
    :param piece: piesa pe care vreau sa o mut
    :param move: linia si coloana pe care vreau sa o mut
    :param board: configuratia actuala a tablei
    :param game: jocul actual
    :param skip: daca am sarit peste vreo piesa
    :return: configuratia tablei dupa ce mut piesa
    Simulez mutarea unei anumite piese
    """
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def GetAllMoves(board, color, game):
    """
    :param board: configuratia actuala a tablei de joc
    :param color: culoarea piesei
    :param game: jocul actual
    :return: lista formata din configuratiile posibile ale tablei dupa ce se pot efectua mutarile posibile
    """
    moves = []
    for p in board.getAllPieces(color):
        valid_moves = board.get_valid_moves(p)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(p.row, p.col)
            new_board = SimulateMove(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves


def MiniMax(board, depth, JMAX, game, noOfNodes):
    """
    :param board: configuratia actuala
    :param depth: adancimea pana a care vreau sa merg
    :param JMAX: verific daca este jucatorul care incearca sa maximizeze
    :param game: jocul curent
    :return: Evaluarea mutarii si tabla
    Primeste tabla cu toate piese la momentul curent, cate mutari vreau sa consider, daca vreau sa maximizez scorul sau sa il minimizez
    """
    if depth == 0 or board.winner() != None:        #daca am ajuns la adancimea maxima sau daca am gasit un castigator
        return board.evaluateScore1(), board      #evaluez configuratia curenta si o returnez
    if JMAX:    #evaluez pentru jucatorul care incearca sa maximizeze scorul
        maxEval = float('-inf')
        bestMove = None
        for move in GetAllMoves(board, game.getBoard().computer_color, game):        #parcurg toate mutarile posibile pentru jucatorul JMAX
            noOfNodes += 1
            evaluation = MiniMax(move, depth - 1, False, game, noOfNodes)[0]
            maxEval = max(maxEval, evaluation)

            if maxEval == evaluation:
                bestMove = move
        return maxEval, bestMove, noOfNodes

    else:       #evaluez pentru jucatorul care incearca sa minimizeze scorul
        minEval = float('inf')
        bestMove = None
        for move in GetAllMoves(board, game.getBoard().user_color, game):        #parcurg toate mutarile posibile pentru jucatorul JMIN
            noOfNodes += 1
            evaluation = MiniMax(move, depth - 1, True, game, noOfNodes)[0]
            minEval = min(minEval, evaluation)

            if minEval == evaluation:
                bestMove = move
        return minEval, bestMove