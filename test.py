import tictactoe as ttt

# board = ttt.initial_state()

# print("Initial Board:")
# print(board)

# print("\nCurrent Player:")
# print(ttt.player(board))

# print("\nAvailable Moves:")
# print(ttt.actions(board))


board = [
    [ttt.X, ttt.O, ttt.X],
    [ttt.EMPTY, ttt.O, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]
]

print(board)
print("Current Player:", ttt.player(board))
print("Moves:", ttt.actions(board))
