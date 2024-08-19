from tictactoe import TicTacToe
from player_type import PlayerType
from mcts import MonteCarloTreeSearch
from node import Node

import time


class TicTacToeCLI:
    def __init__(self, player_pair: tuple[PlayerType, PlayerType]) -> None:
        self.game = TicTacToe(1)
        self.player_1_type, self.player_2_type = player_pair

    def display_board(self):
        print("\nBoard:")
        for row in self.game.board:
            print(" | ".join(["X" if x == 1 else "O" if x == -1 else " " for x in row]))
            print("-" * 9)

    def get_input(self):
        while True:
            try:
                row = int(input("Enter row (1, 2, 3): ")) - 1
                col = int(input("Enter col (1, 2, 3): ")) - 1
                if row not in range(3) or col not in range(3):
                    print("Invalid input. Please enter numbers between 1 and 3.")
                elif self.game.board[row][col] != 0:
                    print("Cell is already taken. Choose another.")
                else:
                    return row, col
            except ValueError:
                print("Invalid input. Please enter numbers.")

    def play(self):
        while not self.game.is_game_over():
            self.display_board()
            print(f"Player {'X' if self.game.current_player == 1 else 'O'}'s turn")
            if self.game.current_player == 1:
                if self.player_1_type == PlayerType.HUMAN:
                    row, col = self.get_input()

                elif self.player_2_type == PlayerType.COMPUTER:
                    node = Node(self.game, None, None)
                    mcts = MonteCarloTreeSearch(node)
                    row, col = mcts.best_action(1000)

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

                else:
                    row, col = self.game.make_random_move()

                self.game.make_move(row, col)

            winner = self.game.get_winner()
            if winner:
                self.display_board()
                print(f"Player {'X' if winner == 1 else 'O'} wins!")
                return
            time.sleep(1)
        self.display_board()
        print("It's a draw!")


if __name__ == "__main__":
    cli = TicTacToeCLI(PlayerType.get_type_pair())
    cli.play()
