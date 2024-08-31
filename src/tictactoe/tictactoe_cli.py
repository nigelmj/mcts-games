from src.game_cli import GameCLI
from src.player import PlayerType
from .tictactoe import TicTacToe


class TicTacToeCLI(GameCLI):
    def __init__(self, player_pair: tuple[PlayerType, PlayerType]) -> None:
        super().__init__(TicTacToe(1), player_pair, "X", "O")

    def display_board(self) -> None:
        print("\nBoard:")
        for row in self.game.board:
            print(" | ".join(["X" if x == 1 else "O" if x == -1 else " " for x in row]))
            print("-" * 9)


if __name__ == "__main__":
    cli = TicTacToeCLI(PlayerType.get_type_pair())
    cli.play(1000)
