from src.game_cli import GameCLI
from src.player import PlayerType
from .connect4 import Connect4


class Connect4CLI(GameCLI):
    def __init__(self, player_pair: tuple[PlayerType, PlayerType]) -> None:
        super().__init__(Connect4(1), player_pair, "X", "O")

    def display_board(self) -> None:
        print("\nBoard:")
        print("   " + "   ".join([str(x) for x in range(1, 8)]))
        print()
        for ind, row in enumerate(self.game.board):
            print(
                str(ind + 1)
                + "  "
                + " | ".join(["X" if x == 1 else "O" if x == -1 else " " for x in row]))
            print("   " + "-" * 25)


if __name__ == "__main__":
    cli = Connect4CLI(PlayerType.get_type_pair())
    cli.play(50000)
