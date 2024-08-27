from src.game import Game


class TicTacToe(Game):
    def __init__(self, player: int) -> None:
        super().__init__([[0 for _ in range(3)] for _ in range(3)], player)

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
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0]

    def set_board(self, board) -> None:
        self.board = board

    def copy(self) -> "TicTacToe":
        new_game = TicTacToe(self.current_player)
        new_game.set_board([row.copy() for row in self.board])
        return new_game
