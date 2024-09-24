from abc import ABC, abstractmethod
import random


class Game(ABC):
    def __init__(self, board: list[list[int]]) -> None:
        self.board = board
        self.set_player(1)

    @abstractmethod
    def make_move(self, row: int, col: int) -> None:
        pass

    @abstractmethod
    def get_legal_moves(self) -> list[tuple[int, int]]:
        pass

    @abstractmethod
    def is_legal_move(self, row: int, col: int) -> bool:
        pass

    def make_random_move(self) -> tuple[int, int]:
        return random.choice(self.get_legal_moves())

    @abstractmethod
    def get_winner(self) -> int:
        pass

    @abstractmethod
    def is_game_over(self) -> bool:
        pass

    @abstractmethod
    def create_game(self) -> "Game":
        pass

    def set_board(self, board: list[list[int]]) -> None:
        self.board = board

    def set_player(self, player: int) -> None:
        self.current_player = player

    def copy(self) -> "Game":
        new_game = self.create_game()
        new_game.set_board([row.copy() for row in self.board])
        new_game.set_player(self.current_player)
        return new_game
