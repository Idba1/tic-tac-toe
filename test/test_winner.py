import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import tictactoe as ttt


def run_test(name, board, expected):
    print(f"\n{name}")
    print("-" * 30)

    for row in board:
        print(row)

    result = ttt.winner(board)

    print("\nExpected :", expected)
    print("Got      :", result)

    if result == expected:
        print("✅ PASS")
    else:
        print("❌ FAIL")


# -------------------------
# Test 1 : Row Win
# -------------------------

board1 = [
    [ttt.X, ttt.X, ttt.X],
    [ttt.O, ttt.EMPTY, ttt.O],
    [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]
]

run_test("Row Win", board1, ttt.X)


# -------------------------
# Test 2 : Column Win
# -------------------------

board2 = [
    [ttt.O, ttt.X, ttt.X],
    [ttt.O, ttt.X, ttt.EMPTY],
    [ttt.O, ttt.EMPTY, ttt.EMPTY]
]

run_test("Column Win", board2, ttt.O)


# -------------------------
# Test 3 : Main Diagonal
# -------------------------

board3 = [
    [ttt.X, ttt.O, ttt.EMPTY],
    [ttt.O, ttt.X, ttt.EMPTY],
    [ttt.EMPTY, ttt.O, ttt.X]
]

run_test("Main Diagonal", board3, ttt.X)


# -------------------------
# Test 4 : Anti Diagonal
# -------------------------

board4 = [
    [ttt.X, ttt.EMPTY, ttt.O],
    [ttt.X, ttt.O, ttt.EMPTY],
    [ttt.O, ttt.EMPTY, ttt.X]
]

run_test("Anti Diagonal", board4, ttt.O)


# -------------------------
# Test 5 : No Winner
# -------------------------

board5 = [
    [ttt.X, ttt.O, ttt.X],
    [ttt.O, ttt.X, ttt.O],
    [ttt.O, ttt.X, ttt.O]
]

run_test("No Winner", board5, None)
