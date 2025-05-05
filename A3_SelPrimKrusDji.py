# =============================== #
# 1. SELECTION SORT (User Input) #
# =============================== #

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("\n--- Selection Sort ---")
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))
sorted_arr = selection_sort(arr)
print("Sorted list:", sorted_arr)

# =================================== #
# 2. DIJKSTRA'S ALGORITHM (User Input)#
# =================================== #

import heapq

def dijkstra(graph, start, end):
    pq = [(0, start)]
    visited = set()
    while pq:
        (cost, node) = heapq.heappop(pq)
        if node == end:
            return cost
        if node in visited:
            continue
        visited.add(node)
        for (neighbor, weight) in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor))
    return float('inf')

print("\n--- Dijkstra's Algorithm ---")
num_edges = int(input("Enter number of edges: "))
graph = {}
for _ in range(num_edges):
    u, v, w = input("Enter edge (format: u v weight): ").split()
    w = int(w)
    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))  # undirected

start = input("Enter start node: ")
end = input("Enter end node: ")
print(f"The shortest distance from {start} to {end} is:", dijkstra(graph, start, end))

# ================================ #
# 3. KRUSKAL'S ALGORITHM (User Input) #
# ================================ #

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph.sort(key=lambda item: item[2])
        parent = list(range(self.V))
        rank = [0] * self.V

        while e < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append((u, v, w))
                self.apply_union(parent, rank, x, y)

        print("Edges in the Minimum Spanning Tree:")
        for u, v, weight in result:
            print(f"{u} - {v}: {weight}")

print("\n--- Kruskal's Algorithm ---")
v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
g = Graph(v)
for _ in range(e):
    u, v, w = map(int, input("Enter edge (u v w): ").split())
    g.add_edge(u, v, w)
g.kruskal_algo()

# ============================== #
# 4. PRIM'S ALGORITHM (User Input) #
# ============================== #

print("\n--- Prim's Algorithm ---")
N = int(input("Enter number of vertices: "))
INF = 99999999
G = []

print("Enter adjacency matrix row by row (use 0 for no edge):")
for i in range(N):
    G.append(list(map(int, input(f"Row {i}: ").split())))

selected = [False] * N
selected[0] = True
no_edge = 0

print("Edge : Weight")
while no_edge < N - 1:
    minimum = INF
    a = b = 0
    for m in range(N):
        if selected[m]:
            for n in range(N):
                if (not selected[n]) and G[m][n]:
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a, b = m, n
    print(f"{a} - {b} : {G[a][b]}")
    selected[b] = True
    no_edge += 1

# ============================== #
# 5. JOB SCHEDULING (User Input) #
# ============================== #

def job_schedule(jobs):
    jobs.sort(key=lambda x: x[1], reverse=True)
    max_deadline = max(job[2] for job in jobs)
    slot = [False] * max_deadline
    profit = 0

    for job in jobs:
        deadline = job[2] - 1
        while deadline >= 0 and slot[deadline]:
            deadline -= 1
        if deadline >= 0:
            slot[deadline] = True
            profit += job[1]
    return profit

print("\n--- Job Scheduling Problem ---")
n = int(input("Enter number of jobs: "))
jobs = []
print("Enter jobs as (id profit deadline):")
for _ in range(n):
    job_id, profit, deadline = map(int, input().split())
    jobs.append((job_id, profit, deadline))

max_profit = job_schedule(jobs)
print("Maximum Profit:", max_profit)
