from src.cli_interface.game_cli import GameCLI
from src.cli_interface.player import PlayerType
from src.games.tictactoe import TicTacToe


class TicTacToeCLI(GameCLI):
    def __init__(self, player_pair: tuple[PlayerType, PlayerType]) -> None:
        super().__init__(TicTacToe(), player_pair, "X", "O")

    def display_state(self) -> None:
        print("\nstate:")
        for row in self.game.state:
            print(" | ".join(["X" if x == 1 else "O" if x == -1 else " " for x in row]))
            print("-" * 9)


if __name__ == "__main__":
    cli = TicTacToeCLI(PlayerType.get_type_pair())
    cli.play(1000)
