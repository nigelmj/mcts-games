from typing import Optional
from game import Game
from math import sqrt, log


class Node:
    def __init__(
        self,
        game: Game,
        parent: Optional["Node"] = None,
        action: Optional[tuple[int, int]] = None,
    ):
        self.game = game
        self.parent = parent
        self.action = action
        self.children = None
        self.wins = 0
        self.simulations = 0

    def is_fully_explored(self) -> bool:
        return self.children is not None and all(
            child.simulations > 0 for child in self.children
        )

    def is_terminal(self) -> bool:
        return self.game.is_game_over()

    def uct(self) -> float:
        if self.simulations == 0 or self.parent is None:
            return float("inf")
        exploitation = self.wins / self.simulations
        exploration = sqrt(2 * log(self.parent.simulations) / self.simulations)
        return exploitation + exploration

    def best_child(self) -> "Node":
        if self.children is None:
            return self
        return max(self.children, key=lambda node: node.uct())

    def get_children(self) -> list["Node"]:
        if self.children is None:
            self.children = []
            if not self.is_terminal() and not self.game.get_legal_moves():
                self.game.current_player *= -1
            for move in self.game.get_legal_moves():
                i, j = move
                child = self.game.copy()
                child.make_move(i, j)
                self.children.append(Node(child, self, move))
        return self.children
