import random


class TicTacToe:
    def __init__(self, player: int) -> None:
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = player

    def make_move(self, row: int, col: int) -> int:
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.current_player = -self.current_player

    def check_winner(self) -> int:
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
        if self.check_winner() != 0:
            return True
        return all(self.board[i][j] != 0 for i in range(3) for j in range(3))

    def valid_moves(self) -> list[tuple[int, int]]:
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0]

    def set_board(self, board: list[list[int]]) -> None:
        self.board = board

    def get_random_move(self) -> tuple[int, int]:
        return random.choice(self.valid_moves())
