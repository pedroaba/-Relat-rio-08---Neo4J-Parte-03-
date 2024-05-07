from neo4j import Driver

from src import Controller
from src.match.match import Match


class MatchController(Controller):
    node_name = "MATCH_PARTY"

    def __init__(self, driver: Driver):
        super(MatchController, self).__init__(driver)

    def create(self, match: Match):
        self.execute_query("CREATE(:<node_name>, {id: $id})", match.to_dict())

    def add_player(self, match: Match):
        self.execute_query(
            """
                MATCH (m:<node_name> {id: $id})
                
                FOREACH (player_id IN $players |
                    MERGE (p:PLAYER {id: player_id})
                    CREATE (p)-[:PLAY_ON]->(m)
                )
            """,
            {
                "id": match.to_dict()["id"],
                "players": match.to_dict()["players"]
            },
        )

    def get(self, match_id: str):
        return self.execute_query(
            "MATCH(m:<node_name> {id: $id}) RETURN m",
            {"id": match_id},
        )

    def get_by_player(self, player_id: str):
        return self.execute_query(
            "MATCH(p:PLAYER {id: $player_id})-[:PLAY_ON]->(m:<node_name>) RETURN m",
            {"player_id": player_id},
        )
