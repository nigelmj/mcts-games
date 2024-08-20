from game import Game


class Othello(Game):
    def __init__(self, player: int) -> None:
        super().__init__([[0 for _ in range(8)] for _ in range(8)], player)
        self.board[3][3] = -1
        self.board[3][4] = 1
        self.board[4][3] = 1
        self.board[4][4] = -1

    def make_move(self, row: int, col: int) -> None:
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.flip_pieces(row, col)
            self.current_player = -self.current_player

    def flip_pieces(self, row: int, col: int) -> None:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                self.flip_direction(row, col, i, j)

    def flip_direction(self, row: int, col: int, i: int, j: int) -> None:
        new_row = row + i
        new_col = col + j
        while (
            0 <= new_row < 8
            and 0 <= new_col < 8
            and self.board[new_row][new_col] == -self.current_player
        ):
            new_row += i
            new_col += j
        if (
            0 <= new_row < 8
            and 0 <= new_col < 8
            and self.board[new_row][new_col] == self.current_player
        ):
            while row != new_row - i or col != new_col - j:
                new_row -= i
                new_col -= j
                self.board[new_row][new_col] = self.current_player

    def get_winner(self) -> int:
        if not self.is_game_over():
            return 0
        count = 0
        for ind, row in enumerate(self.board):
            count += row.count(1)
            count -= row.count(-1)
        return 1 if count > 0 else -1 if count < 0 else 0

    def is_game_over(self) -> bool:
        if not self.get_legal_moves():
            self.current_player = -self.current_player
            if not self.get_legal_moves():
                return True
            self.current_player = -self.current_player
        return False

    def get_legal_moves(self) -> list[tuple[int, int]]:
        moves = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 0 and self.is_legal_move(i, j):
                    moves.append((i, j))
        return moves

    def is_legal_move(self, row: int, col: int) -> bool:
        if self.board[row][col] != 0:
            return False
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.is_legal_direction(row, col, i, j):
                    return True
        return False

    def is_legal_direction(self, row: int, col: int, i: int, j: int) -> bool:
        row += i
        col += j
        if (
            not (0 <= row < 8 and 0 <= col < 8)
            or self.board[row][col] != -self.current_player
        ):
            return False
        while (
            0 <= row < 8
            and 0 <= col < 8
            and self.board[row][col] == -self.current_player
        ):
            row += i
            col += j
        return (
            0 <= row < 8
            and 0 <= col < 8
            and self.board[row][col] == self.current_player
        )

    def set_board(self, board) -> None:
        self.board = board

    def copy(self) -> "Othello":
        new_game = Othello(self.current_player)
        new_game.set_board([row.copy() for row in self.board])
        return new_game
