# Assignment 2
# A* Search Algorithm Implementation with comments

# Heuristic function for A* (h(n))
def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist[n]

# Returns the neighbors and edge weights of a node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    return None

# A* Algorithm function
def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])      # Nodes to be evaluated
    closed_set = set()                # Nodes already evaluated
    g = {}                            # Actual cost from start to the current node
    parents = {}                      # Parent tracking for path reconstruction

    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        # Select the node with the lowest f(n) = g(n) + h(n)
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n is None:
            print("Path does not exist!")
            return None

        # Goal check
        if n == stop_node:
            path = []

            # Backtrack from goal to start using the parent dictionary
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()

            print("Path found: {}".format(path))
            return path

        # Explore neighbors of the current node
        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                # If already discovered, check if a better path exists
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    # Move from closed_set back to open_set if necessary
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        # Move the current node to closed_set after exploring
        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")
    return None

# Graph structure: node → [(neighbor, weight)]
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('A', 2), ('C', 1), ('G', 9)],
    'C': [('B', 1)],
    'D': [('E', 6), ('G', 1)],
    'E': [('A', 3), ('D', 6)],
    'G': [('B', 9), ('D', 1)],
}

# Run the algorithm
aStarAlgo('A', 'G')
