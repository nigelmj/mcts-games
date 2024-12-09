from math import sqrt


c = 2.0


class APVNode:
    def __init__(self, game, parent, action, prior_probability):
        self.game = game
        self.parent = parent
        self.action = action
        self.prior_probability = prior_probability

        self.children = []
        self.value_sum = 0.0
        self.visit_count = 0

    def _ucb_score(self):
        # Unexplored nodes have maximum priority
        if self.visit_count == 0:
            return float("inf")

        top_node = self
        if self.parent:
            top_node = self.parent

        q_score = self.value_sum / self.visit_count
        u_score = (
            c
            * self.prior_probability
            * sqrt(top_node.visit_count)
            / (1 + self.visit_count)
        )
        return q_score + u_score

    def best_child(self) -> "APVNode":
        if not self.children:
            return self
        return max(self.children, key=lambda node: node._ucb_score())

    def is_fully_explored(self) -> bool:
        return self.children != [] and all(
            child.visit_count > 0 for child in self.children
        )

    def is_terminal(self) -> bool:
        return self.game.is_game_over()

    def populate_children(self, normalised_p) -> None:
        if not self.children:
            for move in self.game.get_legal_moves():
                i, j = move
                child = self.game.copy()
                child.make_move(i, j)

                if move == (-1, -1):
                    idx = -1
                else:
                    idx = i * self.game.size2 + j
                prior_probability = normalised_p[0, idx]

                self.children.append(APVNode(child, self, move, prior_probability))
