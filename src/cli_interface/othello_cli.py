from src.cli_interface.game_cli import GameCLI
from src.cli_interface.player import PlayerType
from src.games.othello import Othello


class OthelloCLI(GameCLI):
    def __init__(self, player_pair: tuple[PlayerType, PlayerType]) -> None:
        super().__init__(Othello(), player_pair, "Black", "White")

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


if __name__ == "__main__":
    cli = OthelloCLI(PlayerType.get_type_pair())
    cli.play(10000)
