## connect Four — AI Game Agent

Built as part of the AI lab at IIT Palakkad. Implemented both Alpha-Beta Pruning and Expectimax from scratch in Python, with a tkinter GUI to play the game.

---

## Algorithms

### Alpha-Beta Pruning (vs AI / Human)
An optimized version of Minimax that prunes branches which can't affect the final decision, allowing the agent to search deeper within the time limit. The AI uses **iterative deepening** — it keeps searching deeper and deeper until time runs out, so it always has a valid move ready. It also checks for immediate wins/losses before starting the tree search to avoid unnecessary computation.

### Expectimax (vs Random Player)
When playing against a random opponent, Minimax's worst-case assumption is too pessimistic — a random player doesn't play optimally. Expectimax replaces the minimizing node with a **chance node** that averages over all possible opponent moves with equal probability, which better models random play.

### Heuristic Evaluation Function
Since the full game tree can't be searched, board states are scored using a heuristic that scans every window of 4 cells across all directions — horizontal, vertical, and both diagonals. Each window is scored based on how many pieces the AI or opponent has in it. There's also a bonus for controlling the center column (column 3), since it opens up the most winning lines in Connect Four.

---

## Project Structure

```
├── ConnectFour.py   # Game logic, GUI, and turn management
├── Player.py        # AIPlayer, RandomPlayer, HumanPlayer classes
└── README.md
```

---

## How to Run

### Requirements
```bash
pip install numpy
```
> tkinter comes with standard Python installations.

### Run the game
```bash
python ConnectFour.py <player1> <player2> [--time SECONDS]
```

**Player types:** `ai`, `human`, `random`

### Examples
```bash
# AI vs Human
python ConnectFour.py ai human

# AI vs AI
python ConnectFour.py ai ai

# AI vs Random, with 30s time limit
python ConnectFour.py ai random --time 30
```

---

## Game Controls
- A GUI window opens with the Connect Four board
- Click **Next Move** to advance one turn at a time
- The current player is shown at the top
- The game announces the winner or a draw when it ends
