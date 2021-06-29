"""
Tic Tac Toe Player
"""

import math

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
    WhoTurn = player(board)
    i, j = action
    if board[i][j] is Empty:
        board[i][j] = WhoTurn
    return board


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
    max_action = float("-inf")
    min_action = float("inf")
    max_action = max_value(board)
    
    return max_action

def value(board):
    pass
def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board,action)))
    return v

print(minimax([[X, X, Empty],[Empty, Empty, Empty],[Empty, Empty, Empty]]))