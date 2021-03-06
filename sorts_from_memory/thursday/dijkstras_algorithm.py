#!/bin/python3

import unittest
import networkx as nx


def pick_next_hop(dist_from_src_dict, visited):
    # TODO: This is bad
    shortest_distance = None
    next_node = None
    for node, distance in dist_from_src_dict.items():
        if distance is None or node in visited:
            continue
        update = False
        if shortest_distance is None:
            update = True
        elif distance < shortest_distance:
            update = True
        if update:
            next_node = node
            shortest_distance = distance
    print('picking ', next_node)
    return next_node


def dijkstras_algorithm(G, src, dest):

    print('hello')

    dist_from_src = {node: None for node in G.nodes()}
    dist_from_src[src] = 0
    best_path = {node: [] for node in G.nodes()}
    best_path[src] = [0]
    visited = set()
    unvisited = set(G.nodes())


    while len(unvisited) > 0:
        current_loc = pick_next_hop(dist_from_src, visited)
        current_dist = dist_from_src[current_loc]
        unvisited.remove(current_loc)
        visited.add(current_loc)
        for neigh in G.neighbors(current_loc):
            print('checking neighbour', neigh)
            update = False
            edge_weight = G.get_edge_data(current_loc, neigh)['weight']

            dist_from_cur = edge_weight + current_dist
            neigh_dist = dist_from_src[neigh]
            if neigh_dist is None:
                update = True

            elif neigh_dist > dist_from_cur:
                print('assigning, ', neigh, dist_from_cur)
                update = True

            if update:
                dist_from_src[neigh] = dist_from_cur
                path_to_neigh = best_path[current_loc] + [neigh]
                best_path[neigh] = path_to_neigh



    return dist_from_src[dest], best_path[dest]


class TestDijkstraImplementation(unittest.TestCase):

    def build_example_graph(self):

        G = nx.Graph()
        """
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
