# ========================== #
#       User Input Graph
# ========================== #

def get_graph_from_user():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    
    for _ in range(n):
        node = input("Enter node name (e.g., A): ")
        children = input(f"Enter children of {node} separated by space (or leave blank if none): ")
        graph[node] = children.split() if children else []
    
    return graph

# ========================== #
#       Depth First Search
# ========================== #

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


# =========================== #
#     Breadth First Search
# =========================== #

def bfs(graph, start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


# ============================ #
#         Main Program
# ============================ #

graph = get_graph_from_user()
start_node = input("Enter the start node for traversal: ")

print("\n=== Depth-First Search ===")
dfs(graph, start_node)

print("\n\n=== Breadth-First Search ===")
bfs(graph, start_node)
