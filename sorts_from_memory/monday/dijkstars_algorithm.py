#!/bin/python3
import networkx as nx
import unittest


def pick_next(G, visited, shortest_dist):

    closest = None
    cur_pick = None

    for nodeName in G.nodes():
        if nodeName in visited:
            continue
        distToN = shortest_dist[nodeName]
        if distToN is None:
            continue
        if closest is None:
            closest = distToN
            cur_pick = nodeName
        elif distToN < closest:
            closest = distToN
            cur_pick = nodeName
    return cur_pick


def dijkstras_algorithm(G, src, dest):

    visited = set()
    # unvisited = set(G.nodes())
    # unvisited.remove(src)

    shortest_paths = {src: [src]}
    shortest_dist = {nodeName: None for nodeName in G.nodes()}
    shortest_dist[src] = 0

    while len(visited) < len(G.nodes()):

        cur_n = pick_next(G, visited, shortest_dist)
        cur_d = shortest_dist[cur_n]

        for neigh in G.neighbors(cur_n):
            connection_weight = G.get_edge_data(cur_n, neigh)['weight']
            dist_along_cur = cur_d + connection_weight

            cur_neigh_d = shortest_dist[neigh]
            if cur_neigh_d is None:
                shortest_dist[neigh] = dist_along_cur
                shortest_paths[neigh] = shortest_paths[cur_n] + [neigh]

            elif dist_along_cur < shortest_dist[neigh]:
                shortest_dist[neigh] = dist_along_cur
                shortest_paths[neigh] = shortest_paths[cur_n] + [neigh]

        visited.add(cur_n)

    return shortest_dist[dest], shortest_paths[dest]





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
