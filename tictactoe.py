"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    x_count = 0
    o_count = 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action

    # Invalid move
    if board[i][j] is not EMPTY:
        raise Exception("Invalid Action")

    # Make a deep copy of the board
    new_board = copy.deepcopy(board)

    # Place the current player's mark
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    for row in board:
        if row[0] is not EMPTY and row[0] == row[1] == row[2]:
            return row[0]

    # Check columns
    for j in range(3):
        if (
            board[0][j] is not EMPTY and
            board[0][j] == board[1][j] == board[2][j]
        ):
            return board[0][j]

    # Check main diagonal
    if (
        board[0][0] is not EMPTY and
        board[0][0] == board[1][1] == board[2][2]
    ):
        return board[0][0]

    # Check anti-diagonal
    if (
        board[0][2] is not EMPTY and
        board[0][2] == board[1][1] == board[2][0]
    ):
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Someone has won
    if winner(board) is not None:
        return True

    # Any empty cell left?
    for row in board:
        if EMPTY in row:
            return False

    # Board is full (draw)
    return True


def utility(board):
    """
    Returns 1 if X has won the game,
    -1 if O has won,
    0 otherwise.
    """

    game_winner = winner(board)

    if game_winner == X:
        return 1

    elif game_winner == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
