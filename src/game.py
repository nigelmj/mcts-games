from abc import ABC, abstractmethod
import random


class Game(ABC):
    def __init__(self, board: list[list[int]], player: int) -> None:
        self.board = board
        self.current_player = player

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

    def copy(self) -> "Game":
        new_game = self.create_game()
        new_game.set_board([row.copy() for row in self.board])
        return new_game
