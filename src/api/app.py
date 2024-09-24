from flask import Flask
from flask_cors import CORS
from .routes import connect4_routes, tictactoe_routes, othello_routes


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(connect4_routes.bp)
    app.register_blueprint(tictactoe_routes.bp)
    app.register_blueprint(othello_routes.bp)

    return app
