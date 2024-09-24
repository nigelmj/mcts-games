from src.game import Game


class TicTacToe(Game):
    def __init__(self) -> None:
        super().__init__([[0 for _ in range(3)] for _ in range(3)])

    def create_game(self) -> "TicTacToe":
        return TicTacToe()

    def make_move(self, row: int, col: int) -> None:
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.current_player = -self.current_player

    def get_winner(self) -> int:
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]

        return 0

    def is_game_over(self) -> bool:
        if self.get_winner() != 0:
            return True
        return all(all(cell != 0 for cell in row) for row in self.board)

    def get_legal_moves(self) -> list[tuple[int, int]]:
        return [(i, j) for i in range(3) for j in range(3) if self.is_legal_move(i, j)]

    def is_legal_move(self, row: int, col: int) -> bool:
        return self.board[row][col] == 0
