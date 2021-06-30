"""
Tic Tac Toe Player
"""

import math, copy, random

X = "X"
O = "O"
Empty = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[Empty, Empty, Empty],
            [Empty, Empty, Empty],
            [Empty, Empty, Empty]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_Count = 0
    O_Count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                X_Count = X_Count + 1
            elif board[i][j] == O:
                O_Count = O_Count + 1
    if X_Count > O_Count:
        return O
    return X   


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    _Set = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == Empty:
                _Set.add((i, j))
    return _Set




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    WhoTurn = player(new_board)
    i, j = action
    if new_board[i][j] is Empty:
        new_board[i][j] = WhoTurn
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    possible_wins = [[(0, 0), (0, 1), (0, 2)],
                    [(1, 0), (1, 1), (1, 2)],
                    [(2, 0), (2, 1), (2, 2)],
                    [(0, 0), (1, 0), (2, 0)],
                    [(0, 1), (1, 1), (2, 1)],
                    [(0, 2), (1, 2), (2, 2)],
                    [(0, 0), (1, 1), (2, 2)],
                    [(0, 2), (1, 1), (2, 0)]]

    for possible in possible_wins:
        X_Count = 0
        O_Count = 0
        for i, j in possible:
            if board[i][j] == X:
                X_Count += 1
            if board[i][j] == O:
                O_Count += 1
        if X_Count == 3:
            return X
        if O_Count == 3:
            return O

    return Empty
                


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    possible_actions = actions(board)
    IsSomeOneWin = winner(board)
    if possible_actions == set() or IsSomeOneWin != Empty:
        return True
    return False
#   [[X, X, X],[X, X, X],[X, X, X]]
#   [[Empty, Empty, Empty],[Empty, Empty, Empty],[Empty, Empty, Empty]]

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    WhoWins = winner(board)
    if WhoWins == X:
        return 1
    elif WhoWins == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if board == initial_state():
        # select random cell when it's empty
        x = random.randint(0,2)
        y = random.randint(0,2)
        return x, y
    
    WhoTurn = player(board)
    optimal_value = float("-inf") if WhoTurn == X else float("inf")

    for action in actions(board):
        new_value = minimax_value(result(board, action), optimal_value)

        if WhoTurn == X:
            new_value = max(optimal_value, new_value)

        else:
            new_value = min(optimal_value, new_value)

        if new_value != optimal_value:
            optimal_value = new_value
            optimal_action = action

    return optimal_action

def minimax_value(board, optimal_value):
    """
    Return the minimax value with Alpha-beta pruning for the current player on the board.

    if minimax_value returns value 1, X plays optical and O plays optical, the X will win.
    """
    if terminal(board):
        return utility(board)

    WhoTurn = player(board)
    value = float("-inf") if WhoTurn == X else float("inf")

    for action in actions(board):
        new_value = minimax_value(result(board, action), value)

        if WhoTurn == X:
            # Alpha-beta pruning for the player X
            if new_value > optimal_value:
                return new_value
            value = max(value, new_value)

        else:
            # Alpha-beta pruning for the player O
            if new_value < optimal_value:
                return new_value
            value = min(value, new_value)

    return value
