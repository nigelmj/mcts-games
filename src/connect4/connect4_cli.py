from src.game_cli import GameCLI
from src.player import PlayerType
from .connect4 import Connect4


class Connect4CLI(GameCLI):
    def __init__(self, player_pair: tuple[PlayerType, PlayerType]) -> None:
        super().__init__(Connect4(1), player_pair, "X", "O")

    def display_board(self) -> None:
        print("\nBoard:")
        for row in self.game.board:
            print(" | ".join(["X" if x == 1 else "O" if x == -1 else " " for x in row]))
            print("-" * 15)


if __name__ == "__main__":
    cli = Connect4CLI(PlayerType.get_type_pair())
    cli.play()
