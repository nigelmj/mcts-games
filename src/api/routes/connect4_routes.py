from flask import Blueprint, request, jsonify
from src.games.connect4 import Connect4
from src.mcts.node import Node
from src.mcts.mcts import MonteCarloTreeSearch as MCTS
from src.api.utils import move_to_dict

bp = Blueprint("connect4", __name__, url_prefix="/api/connect4")


@bp.route("/make_move", methods=["POST"])
def make_move():
    print("hello")
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    game = Connect4()
    state = data.get("state")
    player_type = data.get("player_type")
    player = -1 if player_type == "ai" else 1

    game.set_state(state)
    game.set_player(player)

    row, col = -1, -1
    if player_type == "ai":
        root = Node(game, None, None)
        mcts = MCTS()
        ai_move = mcts.best_move(root, 10000)
        row, col = ai_move

    return jsonify(move_to_dict(row, col))
