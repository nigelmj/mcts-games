from flask import Blueprint, request, jsonify
from src.games.tictactoe import TicTacToe
from src.mcts.node import Node
from src.mcts.mcts import MonteCarloTreeSearch as MCTS
from src.api.utils import move_to_dict

bp = Blueprint("tictactoe", __name__, url_prefix="/api/tictactoe")

@bp.route("/make_move", methods=["POST"])
def make_move():
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    game = TicTacToe()
    board = data.get("board")
    player_type = data.get("player_type")
    player = -1 if player_type == "ai" else 1

    game.set_board(board)
    game.set_player(player)

    row, col = -1, -1
    if player_type == "ai":
        root = Node(game, None, None)
        mcts = MCTS()
        ai_move = mcts.best_move(root, 1000)
        row, col = ai_move

    return jsonify(move_to_dict(row, col))
