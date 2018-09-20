#!/bin/python3
import networkx as nx
import unittest


def dijkstras_algorithm(G, src, dest):
    pass


class TestDijkstraImplementation(unittest.TestCase):

    def build_example_graph(self):
        """
        Ascii representation of the graph to run checks on
        .............1........2.......
        ..... (1)---------(5)---(6)...
        ...7../............|..../.....
        ...../.............|.../......
        ...(0)...........1.|../.10....
        .....\.............|./........
        ...3..\............|/.........
        ......(2)---------(4).........
        .............2................
        """

        G = nx.Graph()

        edges = [
            (0, 1, 7),
            (0, 2, 3),
            (1, 5, 1),
            (2, 5, 10),
            (2, 4, 2),
            (4, 5, 1),
            (4, 6, 10),
            (5, 6, 2),
        ]

        G.add_weighted_edges_from(edges)

        return G

    def add_detour(self, G, origin, end, num_to_add, weight):

        first_new_node = max(G.nodes()) + 1
        detour_edges = []

        nodes_to_add = [origin] + [first_new_node + i for i in range(num_to_add)] + [end]
        for n1, n2 in zip(nodes_to_add[:-1], nodes_to_add[1:]):
            detour_edges.append((n1, n2, weight))

        print('adding', detour_edges)

        G.add_weighted_edges_from(detour_edges)
        return G

    def test_djkestra(self):
        G = self.build_example_graph()
        shortest_dist, shortest_path = dijkstras_algorithm(G, 0, 6)
        self.assertEqual(shortest_dist, 8)
        self.assertEqual(shortest_path, [0, 2, 4, 5, 6])

    def test_detour(self):

        G = self.build_example_graph()
        G = self.add_detour(G, 4, 6, 1, 1)

        shortest_dist, shortest_path = dijkstras_algorithm(G, 0, 6)
        print(shortest_dist, shortest_path)
        self.assertEqual(shortest_dist, 7)
        self.assertEqual(shortest_path, [0, 2, 4, 7, 6])


if __name__ == "__main__":
    unittest.main()
