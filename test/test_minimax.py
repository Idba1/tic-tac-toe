import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import tictactoe as ttt


def run_test(name, board):
    print(f"\n{name}")
    print("-" * 35)

    for row in board:
        print(row)

    print("\nCurrent Player :", ttt.player(board))
    print("Best Move      :", ttt.minimax(board))


# -------------------------
# Test 1
# X has an immediate winning move
# -------------------------

board1 = [
    [ttt.X, ttt.O, ttt.X],
    [ttt.O, ttt.X, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.O]
]

run_test("Winning Move", board1)


# -------------------------
# Test 2
# O must block X
# -------------------------

board2 = [
    [ttt.X, ttt.X, ttt.EMPTY],
    [ttt.O, ttt.EMPTY, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.O]
]

run_test("Blocking Move", board2)


# -------------------------
# Test 3
# Empty Board
# -------------------------

board3 = ttt.initial_state()

run_test("Initial Board", board3)


# -------------------------
# Test 4
# Terminal Board
# -------------------------

board4 = [
    [ttt.X, ttt.X, ttt.X],
    [ttt.O, ttt.O, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]
]

run_test("Finished Game", board4)