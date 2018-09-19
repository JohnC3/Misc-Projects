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

def pick_next(dist_to_node, visited):
    cur = None

    for k in dist_to_node:
        if dist_to_node[k] is None:
            continue
        if k in visited:
            continue
        if cur is None:
            cur = k
        elif dist_to_node[k] < dist_to_node[cur]:
            cur = k
    return cur

def dijkstras_shortest_path(G, origin, endpt):

    # Establish prelim distance to each node
    dist_to_node = {}

    dist_to_node = {origin: 0}
    unvisited = set()
    for node in G.nodes():
        dist_to_node[node] = None # Use None for INF
        unvisited.add(node)
    dist_to_node[origin] = 0
    best_path = {origin: [origin]}
    visited = set()
    cur = origin


    while len(unvisited) > 0:
        cur = pick_next(dist_to_node, visited)
        print(f'will now look at {cur}')
        dist_to_cur = dist_to_node[cur]
        cur_best_path = best_path[cur]
        assert cur_best_path is not None

        # Find the lowest cost path thing,
        for neigh in G.neighbors(cur):
            if neigh in visited:
                continue
            print('path to cur was ', best_path[cur], 'dist to cur was ', dist_to_node[cur])
            shorter_path = False
            print('look at neighbour ', neigh)

            edge_cost = G.get_edge_data(cur, neigh)['weight']
            dist_this_path = dist_to_cur + edge_cost

            if dist_to_node[neigh] is None:
                shorter_path = True
            elif dist_this_path < dist_to_node[neigh]:
                shorter_path = True

            if shorter_path:
                print("#######################")

                path_to_neigh = [i for i in cur_best_path]
                path_to_neigh.append(neigh)
                dist_to_node[neigh] = dist_this_path
                print(f'added {dist_this_path} to {neigh}')
                assert neigh in dist_to_node
                print('path_to_neigh', path_to_neigh)
                best_path[neigh] = path_to_neigh



        visited.add(cur)
        unvisited.remove(cur)
    print('got to endpt ', dist_to_node[endpt])
    print('return ', best_path[endpt])
    return dist_to_node[endpt], best_path[endpt]


dijkstras_shortest_path(G, 0, 6)
