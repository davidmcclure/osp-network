

import networkx as nx

from osp.citations.hlom.models.citation import HLOM_Citation
from playhouse.postgres_ext import ServerSide


class Network:


    def __init__(self, graph=None):

        """
        Set (or initialize) a NetworkX graph instance.

        Args:
            graph (networkx.Graph|None)
        """

        self.graph = graph if graph else nx.Graph()


    def build(self):

        """
        Construct the network.
        """

        # Select all cited HLOM records.
        nodes = (
            HLOM_Citation
            .select(HLOM_Citation.record)
            .distinct(HLOM_Citation.record)
        )

        # Add each record as a node.
        for node in ServerSide(nodes):
            self.graph.add_node(
                node.record.control_number,
                title=node.record.title(),
                author=node.record.author()
            )
