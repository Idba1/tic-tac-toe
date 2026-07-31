import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import tictactoe as ttt



board = [
    [ttt.X, ttt.O, ttt.X],
    [ttt.O, ttt.EMPTY, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]
]

print("Original Board:")
for row in board:
    print(row)

new_board = ttt.result(board, (1, 1))

print("\nNew Board:")
for row in new_board:
    print(row)

print("\nOriginal Board Again:")
for row in board:
    print(row)
