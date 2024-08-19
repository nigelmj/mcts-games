from node import Node
import random


class MonteCarloTreeSearch:
    def __init__(self, root) -> None:
        self.root = root

    def best_action(self, simulations_number: int) -> int:
        for _ in range(simulations_number):
            node = self._selection()
            expanded_node = self._expansion(node)
            terminal_node = self._simulation(expanded_node)
            self._backpropagation(terminal_node)
        best_child = max(self.root.get_children(), key=lambda child: child.simulations)
        return best_child.action

    def _selection(self) -> Node:
        node = self.root
        while node.is_fully_explored() and not node.is_terminal():
            node = node.best_child()
        return node

    def _expansion(self, selected_node: Node) -> Node:
        if selected_node.is_terminal():
            return selected_node

        children = selected_node.get_children()
        unexplored_children = [child for child in children if child.simulations == 0]
        return random.choice(unexplored_children)

    def _simulation(self, expanded_node: Node) -> Node:
        while not expanded_node.is_terminal():
            expanded_node = random.choice(expanded_node.get_children())
        return expanded_node

    def _backpropagation(self, terminal_node: Node) -> None:
        player = terminal_node.game.get_winner() * -1
        node = terminal_node
        while node is not None:
            if player != 0:
                if node.game.current_player == player:
                    node.wins += 1
                else:
                    node.wins -= 1
            node.simulations += 1
            node = node.parent
