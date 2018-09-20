
#!/bin/python3
import networkx as nx
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

print(G.adj)


def pick_next_hop(dist_from_src_dict):

    shortest_distance = None
    next_node = None
    for node, distance in dist_from_src_dict.items():

        if shortest_distance is None or distance < shortest_distance:
            next_node = node
            shortest_distance = distance
    print('picking ', next_node)
    return next_node


def dijkstras_algorithm(G, src, dest):

    dist_from_src = {node: None for node in G.nodes()}
    dist_from_src[src] = 0
    best_path = {node: [] for node in G.nodes()}
    best_path[src] = [0]
    visited = set()
    unvisited = set()

    current_loc = src
    while len(unvisited) > 0:
        current_dist = dist_from_src[current_loc]
        unvisited.remove(current_loc)
        visited.add(current_loc)
        for neigh in G.neighbors(current_loc):
            edge_weight = G.get_edge_data(current_loc, neigh)['weight']
            dist_from_cur = edge_weight + current_dist
            neigh_dist = dist_from_src[neigh]
            if neigh_dist is None or neigh_dist > dist_from_cur:
                dist_from_src[neigh] = dist_from_cur
                path_to_neigh = best_path[current_loc] + [neigh]
                best_path[neigh] = path_to_neigh

        current_loc = pick_next_hop(dist_from_src)

    return dist_from_src[dest]


dijkstras_algorithm(G, 0, 6)
