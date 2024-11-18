from src.mcts.node import Node
import random
import time


class MonteCarloTreeSearch:
    def __init__(self) -> None:
        pass

    def best_move(self, root: Node, simulations_number: int) -> tuple[int, int]:
        start = time.time()
        for _ in range(simulations_number):
            node = self._selection(root)
            expanded_node = self._expansion(node)
            result = self._simulation(expanded_node)
            self._backpropagation(expanded_node, result * root.game.current_player)
        best_child = max(root.get_children(), key=lambda child: child.simulations)

        if not best_child.move:
            return (-1, -1)
        for child in root.get_children():
            print(child.move, child.wins, child.simulations)
        print()
        print("Time:", time.time() - start)
        return best_child.move

    def _selection(self, root: Node) -> Node:
        node = root
        while node.is_fully_explored() and not node.is_terminal():
            node = node.best_child()
        return node

    def _expansion(self, selected_node: Node) -> Node:
        if selected_node.is_terminal():
            return selected_node

        children = selected_node.get_children()
        unexplored_children = [child for child in children if child.simulations == 0]
        return random.choice(unexplored_children)

    def _simulation(self, expanded_node: Node) -> int:
        simulated_game = expanded_node.game.copy()
        while not simulated_game.is_game_over():
            move = random.choice(simulated_game.get_legal_moves())
            simulated_game.make_move(*move)
        return simulated_game.get_winner()

    def _backpropagation(self, terminal_node: Node, result: int) -> None:
        node = terminal_node
        while node is not None:
            node.wins += result
            node.simulations += 1
            node = node.parent
