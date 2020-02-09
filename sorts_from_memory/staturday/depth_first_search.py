import networkx as nx




def bredth_first_search(graph, root, target):

    visited = set()

    queue = [root]

    while len(queue) > 0:

        next = queue.pop()
        print(next)

        if next == target:
            return next

        visited.add(next)

        for adj in nx.neighbors(graph, next):
            if adj not in visited:

                queue.append(adj)



if __name__ == "__main__":
    social_net = nx.barabasi_albert_graph(20, 1)
    grid = nx.grid_2d_graph(20, 5)

    nx.draw_spring(grid)

    print(grid.nodes())
    print(grid.edges())
    bredth_first_search(grid, (0, 0), (19, 4))
