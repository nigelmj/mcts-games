from abc import ABC, abstractmethod
import random


class Game(ABC):
    def __init__(self, player: int) -> None:
        self.current_player = player

    @abstractmethod
    def make_move(self, row: int, col: int) -> int:
        pass

    @abstractmethod
    def get_legal_moves(self) -> list[tuple[int, int]]:
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
    def copy(self, board):
        pass
