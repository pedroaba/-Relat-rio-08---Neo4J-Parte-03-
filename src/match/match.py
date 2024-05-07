from src.player.player import Player


class Match:
    def __init__(self, _id: str, players: list[Player]):
        self._id = _id
        self._players = players

    def to_dict(self):
        return {
            "id": self._id,
            "players": [player.to_dict()["id"] for player in self._players]
        }
