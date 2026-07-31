import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import tictactoe as ttt


board = ttt.initial_state()

print("Initial Board:")
print(board)

print("\nCurrent Player:")
print(ttt.player(board))

print("\nAvailable Moves:")
print(ttt.actions(board))
