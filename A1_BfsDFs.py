# ========================== #
#      Common Graph (Tree)
# ========================== #

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# ========================== #
#       Depth First Search
# ========================== #

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')  # Process node

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


print("=== Depth-First Search ===")
dfs(graph, 'A')

print("\n")  # Spacer between outputs


# =========================== #
#     Breadth First Search
# =========================== #

def bfs(graph, start):
    visited = []  # List to track visited nodes
    queue = []    # BFS queue

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=' ')  # Process node

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


print("=== Breadth-First Search ===")
bfs(graph, 'A')
