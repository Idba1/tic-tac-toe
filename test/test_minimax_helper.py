import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import tictactoe as ttt


board = [
    [ttt.X, ttt.O, ttt.X],
    [ttt.O, ttt.X, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.O]
]

print("Board:")
for row in board:
    print(row)

print()

print("Current Player :", ttt.player(board))
print("Terminal       :", ttt.terminal(board))

print()

print("max_value :", ttt.max_value(board))
print("min_value :", ttt.min_value(board))