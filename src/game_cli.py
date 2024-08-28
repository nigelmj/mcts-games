from abc import ABC, abstractmethod
from .player import PlayerType
from .node import Node
from .mcts import MonteCarloTreeSearch
from .game import Game

import time


class GameCLI(ABC):
    def __init__(
        self, game: Game, player_pair: tuple[PlayerType, PlayerType], player_1, player_2
    ) -> None:
        self.game = game
        self.player_1_type, self.player_2_type = player_pair
        self.player_1 = player_1
        self.player_2 = player_2

    @abstractmethod
    def display_board(self) -> None:
        raise NotImplementedError

    def get_input(self) -> tuple[int, int]:
        row_end = len(self.game.board)
        col_end = len(self.game.board[0])

        while True:
            try:
                row = int(input(f"Enter row (1-{row_end}): ")) - 1
                col = int(input(f"Enter col (1-{col_end}): ")) - 1
                if row not in range(6) or col not in range(7):
                    print(
                        f"Invalid input. Please enter numbers between 1 and {row_end}.\nand between 1 and {col_end}."
                    )
                elif self.game.board[row][col] != 0:
                    print("Cell is already taken. Please choose another.")
                elif not self.game.is_legal_move(row, col):
                    print("Invalid move. Please choose another.")
                else:
                    return row, col
            except ValueError:
                print("Invalid input. Please enter numbers.")

    def play(self) -> None:
        while not self.game.is_game_over():
            self.display_board()
            print(
                f"Player {self.player_1 if self.game.current_player == 1 else self.player_2}'s turn"
            )
            if self.game.current_player == 1:
                if self.player_1_type == PlayerType.HUMAN:
                    row, col = self.get_input()

                elif self.player_1_type == PlayerType.COMPUTER:
                    node = Node(self.game, None, None)
                    mcts = MonteCarloTreeSearch(node)
                    row, col = mcts.best_action(1000)
                    print(f"Computer plays: {row + 1}, {col + 1}")

                else:
                    row, col = self.game.make_random_move()

                self.game.make_move(row, col)

            elif self.game.current_player == -1:
                if self.player_2_type == PlayerType.HUMAN:
                    row, col = self.get_input()

                elif self.player_2_type == PlayerType.COMPUTER:
                    node = Node(self.game, None, None)
                    mcts = MonteCarloTreeSearch(node)
                    row, col = mcts.best_action(1000)
                    print(f"Computer plays: {row + 1}, {col + 1}")

                else:
                    row, col = self.game.make_random_move()

                self.game.make_move(row, col)

            winner = self.game.get_winner()
            if winner:
                self.display_board()
                print(f"Player {self.player_1 if winner == 1 else self.player_2} wins!")
                return
            time.sleep(1)
        self.display_board()
        print("It's a draw!")
