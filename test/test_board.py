import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import tictactoe as ttt

board = [
    [ttt.X, ttt.O, ttt.X],
    [ttt.EMPTY, ttt.O, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]
]

print(board)
print("Current Player:", ttt.player(board))
print("Moves:", ttt.actions(board))
