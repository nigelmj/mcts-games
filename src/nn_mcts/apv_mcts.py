from src.games.game import Game
from src.nn_mcts.apv_node import APVNode
from tensorflow.keras.models import Model
import random
import numpy as np


class APVMCTS:
    def __init__(self, root: APVNode, model: Model, num_simulations: int) -> None:
        self.root = root
        self.model = model
        self.num_simulations = num_simulations

    def compute_improved_policy(self) -> np.ndarray:
        for _ in range(self.num_simulations):
            node = self._selection(self.root)
            expanded_node = self._expansion(node)
            result = self._evaluation(expanded_node)
            self._backpropagation(expanded_node, result)

        total_visits = sum(child.visit_count for child in self.root.children)
        policy = np.zeros(self.root.game.size1 * self.root.game.size2 + 1)

        for child in self.root.children:
            if child.action:
                if child.action == (-1, -1):
                    policy[-1] = 1.0
                else:
                    action_idx = child.action[0] * self.root.game.size2 + child.action[1]
                    policy[action_idx] = child.visit_count / total_visits

        policy /= np.sum(policy)
        return policy

    def _selection(self, root: APVNode) -> APVNode:
        node = root
        while node.is_fully_explored() and not node.is_terminal():
            node = node.best_child()
        return node

    def _expansion(self, selected_node: APVNode) -> APVNode:
        if selected_node.is_terminal() or not selected_node.children:
            return selected_node

        children = selected_node.children
        unexplored_children = [child for child in children if child.visit_count == 0]
        return random.choice(unexplored_children)

    def _evaluation(self, expanded_node: APVNode) -> float:
        encoded_state = expanded_node.game.encode_state()
        policy, value = self.model.predict(encoded_state, verbose=0)

        if expanded_node.game.is_game_over():
            return value
        normalised_p = self._normalise_policy(policy, expanded_node.game)
        expanded_node.populate_children(normalised_p)
        return value

    def _backpropagation(self, terminal_node: APVNode, result: float) -> None:
        node = terminal_node
        while node is not None:
            node.value_sum += abs(result) if node.game.current_player != result else -abs(result)
            node.visit_count += 1
            node = node.parent

    def _normalise_policy(self, policy: np.ndarray, game: Game) -> np.ndarray:
        # Mask illegal moves
        masked_policy = policy * game.legal_moves_mask()
        sum_masked = np.sum(masked_policy)
        # Normalise to sum to 1
        normalised_policy = masked_policy / sum_masked
        return normalised_policy
