# 🎮 Tic-Tac-Toe AI using Minimax Algorithm

An Artificial Intelligence Lab project developed in Python. This project implements an unbeatable Tic-Tac-Toe AI using the **Minimax Algorithm**, allowing a human player to compete against an optimal AI.

---

## 📌 Project Information

- **Course:** SE334 - Artificial Intelligence Lab
- **Semester:** Summer 2026
- **Project:** Tic-Tac-Toe AI
- **Algorithm Used:** Minimax Algorithm
- **Language:** Python 3
- **GUI Library:** Pygame

---

# 📂 Project Structure

```
project/
│
├── tictactoe.py          # Main game logic
├── runner.py             # GUI and game runner
├── requirements.txt
├── README.md
├── OpenSans-Regular.ttf
│
└── tests/
    ├── test_player.py
    ├── test_actions.py
    ├── test_result.py
    ├── test_winner.py
    ├── test_terminal_utility.py
    └── test_minimax.py
```

---

# 🎯 Project Objective

The objective of this project is to develop an AI agent capable of playing Tic-Tac-Toe optimally using the **Minimax Algorithm**.

The AI evaluates every possible future move before making a decision, ensuring that it never loses if both players play optimally.

---

# 🧠 Implemented Functions

The following functions have been implemented inside `tictactoe.py`.

| Function | Description |
|----------|-------------|
| `initial_state()` | Creates an empty board |
| `player()` | Determines whose turn it is |
| `actions()` | Returns all possible legal moves |
| `result()` | Returns a new board after making a move |
| `winner()` | Determines the winner |
| `terminal()` | Checks whether the game is over |
| `utility()` | Returns game score (1, -1, 0) |
| `max_value()` | Maximizing step of Minimax |
| `min_value()` | Minimizing step of Minimax |
| `minimax()` | Returns the optimal move |

---

# 🤖 Minimax Algorithm

The Minimax algorithm is an adversarial search algorithm used for two-player games.

### Maximizing Player

- Player X
- Tries to maximize the utility value.

### Minimizing Player

- Player O
- Tries to minimize the utility value.

### Utility Values

| Result | Score |
|---------|------:|
| X Wins | 1 |
| Draw | 0 |
| O Wins | -1 |

The algorithm recursively explores all possible game states and selects the move that guarantees the best possible outcome.

---

# ⚙️ Requirements

Python 3.x

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Game

Run

```bash
python runner.py
```

Choose whether to play as:

- X
- O

The AI will automatically make its move.

---

# 🧪 Running Tests

Each function has its own test file.

Example:

```bash
python tests/test_player.py
```

```bash
python tests/test_actions.py
```

```bash
python tests/test_result.py
```

```bash
python tests/test_winner.py
```

```bash
python tests/test_terminal_utility.py
```

```bash
python tests/test_minimax.py
```

---

# 📸 Expected Features

- Human vs AI gameplay
- GUI using Pygame
- AI never loses
- Detects wins correctly
- Detects draw correctly
- Uses recursive Minimax search
- Returns optimal moves

---

# 🐞 Testing

The project has been tested for:

- Player selection
- Legal move generation
- Board updates
- Winner detection
- Terminal state detection
- Utility evaluation
- Optimal Minimax move selection

---

# 🚀 Future Improvements

Possible future improvements include:

- Alpha-Beta Pruning
- Difficulty Levels
- Move Ordering
- Memoization
- AI vs AI Mode
- Scoreboard
- Game History

---

# 📚 Learning Outcomes

Through this project, we learned:

- Adversarial Search
- Game Trees
- Recursive Algorithms
- Minimax Algorithm
- State Space Search
- Decision Making in AI
- Python Programming
- Pygame Basics

---

---

# 👩‍💻 Author

**Monira Islam**

B.Sc. in Software Engineering

Daffodil International University

---

# 👨‍💻 Developed For

Artificial Intelligence Lab (SE334)

Summer 2026

Daffodil International University
