from othello import Othello
from player import PlayerType
from mcts import MonteCarloTreeSearch
from node import Node

import time


class OthelloCLI:
    def __init__(self, player_pair: tuple[PlayerType, PlayerType]) -> None:
        self.game = Othello(1)
        self.player_1_type, self.player_2_type = PlayerType.get_type_pair()

    def display_board(self) -> None:
        print("\nBoard:")
        print("   " + "   ".join([str(x) for x in range(1, 9)]))
        print()
        for ind, row in enumerate(self.game.board):
            print(
                str(ind + 1)
                + "  "
                + " | ".join(["B" if x == 1 else "W" if x == -1 else " " for x in row])
            )
            print("   " + "-" * 30)

    def get_input(self) -> tuple[int, int]:
        while True:
            try:
                row = int(input("Enter row (1-8): ")) - 1
                col = int(input("Enter col (1-8): ")) - 1
                if row not in range(8) or col not in range(8):
                    print("Invalid input. Please enter numbers between 1 and 8.")
                elif self.game.board[row][col] != 0:
                    print("Cell is already taken. Choose another.")
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
                f"Player {'Black' if self.game.current_player == 1 else 'White'}'s turn"
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
                print(f"Player {'Black' if winner == 1 else 'White'} wins!")
                return
            time.sleep(1)
        self.display_board()
        print("It's a draw!")


if __name__ == "__main__":
    cli = OthelloCLI(PlayerType.get_type_pair())
    cli.play()
