import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import tictactoe as ttt


def run_test(name, board):
    print(f"\n{name}")
    print("-" * 30)

    for row in board:
        print(row)

    print("\nWinner   :", ttt.winner(board))
    print("Terminal :", ttt.terminal(board))
    print("Utility  :", ttt.utility(board))


# --------------------------
# X Wins
# --------------------------

board1 = [
    [ttt.X, ttt.X, ttt.X],
    [ttt.O, ttt.O, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]
]

run_test("X Wins", board1)


# --------------------------
# O Wins
# --------------------------

board2 = [
    [ttt.O, ttt.X, ttt.X],
    [ttt.O, ttt.X, ttt.EMPTY],
    [ttt.O, ttt.EMPTY, ttt.EMPTY]
]

run_test("O Wins", board2)


# --------------------------
# Draw
# --------------------------

board3 = [
    [ttt.X, ttt.O, ttt.X],
    [ttt.O, ttt.X, ttt.O],
    [ttt.O, ttt.X, ttt.O]
]

run_test("Draw", board3)


# --------------------------
# Game Not Finished
# --------------------------

board4 = [
    [ttt.X, ttt.O, ttt.EMPTY],
    [ttt.EMPTY, ttt.X, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.O]
]

run_test("Game Running", board4)