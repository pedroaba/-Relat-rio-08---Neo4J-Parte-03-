from neo4j import Driver, Query
from typing import Any, LiteralString


class Controller:
    label = "DEFAULT_LABEL"
    node_name = "DEFAULT_NODE_NAME"
    relation_name = "DEFAULT_RELATION_NAME"

    def __init__(self, driver: Driver):
        self.driver = driver

    def execute_query(self, query, parameters: Any = None):
        data = []

        formatted_query: LiteralString = query.replace(
            "<node_name>", self.node_name
        )

        with self.driver.session() as session:
            results = session.run(
                formatted_query,
                parameters
            )
            for record in results:
                data.append(record)
        return data
