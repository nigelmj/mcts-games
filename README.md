# MCTS Games Project

This repository contains an implementation of the Monte Carlo Tree Search (MCTS) algorithm, along 
with three classic board games: Tic Tac Toe, Connect 4, and Othello. The project was created for 
self-learning purposes to understand and experiment with the MCTS algorithm.

## Project Overview

- MCTS Algorithm: An implementation of the Monte Carlo Tree Search algorithm.
- Games:
  - Tic Tac Toe
  - Connect 4
  - Othello
- API: Flask-based APIs to get the best move for each game.

## Purpose

This project serves as a personal learning exercise to explore artificial intelligence in game theory. 
It focuses on implementing the MCTS algorithm, applying it to classic board games, and creating RESTful 
APIs using Flask. The goal is to gain practical experience with AI algorithms and their application in 
different game scenarios.

## Features

- MCTS algorithm implementation
- Game logic for Tic Tac Toe, Connect 4, and Othello
- Flask APIs to retrieve the best move for each game

## Usage

### Prerequisites

* Python 3.7+
* Flask

### Installation

1. Clone the repository:

```sh
git clone https://github.com/nigelmj/mcts-games.git
cd mcts-games-project
```

2. Install required packages:

```sh
pip install -r requirements.txt
```

### Running the Games
To play the games locally:

1. Run the desired game script:

```python
python3 -m src.cli_interface.tic_tac_toe_cli
python3 -m src.cli_interface.connect4_cli
python3 -m src.cli_interface.othello_cli
```

2. Follow the on-screen instructions to make moves.

### Using the API
1. To start the Flask server and use the API:

Run the Flask application:

```python
python3 run.py
```

2. The API will be available at http://localhost:5000

### API Endpoints:

* POST /api/tictactoe/make_move
* POST /api/connect4/make_move
* POST /api/othello/make_move

These endpoints expect the current game state and player in the request body.

## Note

This project is primarily for educational purposes and may not be optimized for production use.

## Contributing

As this is a personal learning project, contributions are not actively sought. However, feedback and suggestions are always welcome!
