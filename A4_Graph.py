class Graph:
    def __init__(self, vertices):  # Corrected __init__ method
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_safe(self, v, c, color):
        for i in self.graph[v]:
            if color[i] == c:
                return False
        return True  # Moved outside the loop

    def graph_color_util(self, m, color, v):
        if v == self.V:
            return True
        for c in range(1, m + 1):
            if self.is_safe(v, c, color):
                color[v] = c
                if self.graph_color_util(m, color, v + 1):
                    return True
                color[v] = 0  # Backtrack
        return False

    def graph_color(self, m):
        color = [0] * self.V
        if not self.graph_color_util(m, color, 0):
            print("Solution does not exist")
            return False
        for i in range(self.V):
            print("Vertex", i, ":", "Color", color[i])
        return True

# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.graph_color(3)  # Try coloring with 3 colors




# -----------------------------
# User Input Section
# -----------------------------

# Input number of vertices
v = int(input("Enter number of vertices: "))
g = Graph(v)

# Input number of edges
e = int(input("Enter number of edges: "))

print("Enter edges as pairs (e.g., '0 1'):")

# Add edges
for _ in range(e):
    u, v = map(int, input().split())
    g.add_edge(u, v)

# Input number of colors to try
m = int(input("Enter number of colors: "))

# Solve graph coloring
g.graph_color(m)
