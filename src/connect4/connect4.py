from src.game import Game


class Connect4(Game):
    def __init__(self) -> None:
        super().__init__([[0 for _ in range(7)] for _ in range(6)])

    def create_game(self) -> "Connect4":
        return Connect4()

    def make_move(self, row: int, col: int) -> None:
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.current_player = -self.current_player

    def get_winner(self) -> int:
        for row in range(6):
            for col in range(7):
                if self.board[row][col] != 0:
                    if col + 3 < 7 and all(
                        self.board[row][col + i] == self.board[row][col]
                        for i in range(4)
                    ):
                        return self.board[row][col]

                    if row + 3 < 6 and all(
                        self.board[row + i][col] == self.board[row][col]
                        for i in range(4)
                    ):
                        return self.board[row][col]

                    if (
                        row + 3 < 6
                        and col + 3 < 7
                        and all(
                            self.board[row + i][col + i] == self.board[row][col]
                            for i in range(4)
                        )
                    ):
                        return self.board[row][col]

                    if (
                        row - 3 >= 0
                        and col + 3 < 7
                        and all(
                            self.board[row - i][col + i] == self.board[row][col]
                            for i in range(4)
                        )
                    ):
                        return self.board[row][col]
        return 0

    def is_game_over(self) -> bool:
        if self.get_winner() != 0:
            return True
        return all(all(cell != 0 for cell in row) for row in self.board)

    def get_legal_moves(self) -> list[tuple[int, int]]:
        return [(i, j) for i in range(6) for j in range(7) if self.is_legal_move(i, j)]

    def is_legal_move(self, row: int, col: int) -> bool:
        return self.board[row][col] == 0 and (row == 5 or self.board[row + 1][col] != 0)
