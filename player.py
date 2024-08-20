from enum import Enum


class PlayerType(Enum):
    HUMAN = 1
    COMPUTER = 2
    RANDOM = 3

    @staticmethod
    def get_type_pair() -> tuple["PlayerType", "PlayerType"]:
        player_1 = PlayerType.COMPUTER
        player_2 = PlayerType.HUMAN

        return player_1, player_2
