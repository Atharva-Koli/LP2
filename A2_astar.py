# Assignment 2
# A* Search Algorithm Implementation with user input and detailed comments

def heuristic(n, goal_node):
    # Ask user to input heuristic values once at start
    return H_dist[n]

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    return None

def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])    # Nodes to evaluate
    closed_set = set()              # Already evaluated nodes
    g = {}                          # Actual cost from start node
    parents = {}                    # For tracking shortest path

    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        # Choose node with lowest f(n) = g(n) + h(n)
        for v in open_set:
            if n is None or g[v] + heuristic(v, stop_node) < g[n] + heuristic(n, stop_node):
                n = v

        if n is None:
            print("Path does not exist!")
            return None

        # If goal node is reached, build path
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print("Path found: {}".format(path))
            return path

        # Check neighbors
        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")
    return None

# ------------------- USER INPUT SECTION ----------------------

# Input: number of nodes
num_nodes = int(input("Enter number of nodes in the graph: "))
Graph_nodes = {}

print("\nEnter neighbors for each node in the format: neighbor,weight (comma-separated).")
print("Example input for node A: B,2 C,3 (meaning A -> B (2), A -> C (3))\n")

# Create graph dictionary
for _ in range(num_nodes):
    node = input("Enter node name: ").strip()
    neighbors_input = input(f"Enter neighbors of {node}: ").strip().split()
    Graph_nodes[node] = []
    for pair in neighbors_input:
        try:
            neighbor, weight = pair.split(',')
            Graph_nodes[node].append((neighbor.strip(), int(weight)))
        except:
            print("Invalid format. Skipping:", pair)

# Input heuristic values
print("\nEnter heuristic values for each node to the goal (h(n)):")
H_dist = {}
for node in Graph_nodes.keys():
    H_dist[node] = int(input(f"Heuristic value for {node}: "))

# Start and Goal input
start = input("\nEnter start node: ").strip()
goal = input("Enter goal node: ").strip()

# Run the algorithm
aStarAlgo(start, goal)
