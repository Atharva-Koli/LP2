# -----------------------------------------
# 1. SELECTION SORT
# -----------------------------------------
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

my_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(my_list)
print("Selection Sort Output:")
print(sorted_list)
print("\n")

# -----------------------------------------
# 2. DIJKSTRA'S ALGORITHM
# -----------------------------------------
import heapq

def dijkstra(graph, start, end):
    pq = [(0, start)]
    visited = set()
    while pq:
        cost, curr_node = heapq.heappop(pq)
        if curr_node == end:
            return cost
        if curr_node in visited:
            continue
        visited.add(curr_node)
        for next_node, edge_cost in graph[curr_node]:
            if next_node not in visited:
                heapq.heappush(pq, (cost + edge_cost, next_node))
    return float("inf")

graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('B', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

shortest_distance = dijkstra(graph, 'B', 'D')
print("Dijkstra's Algorithm Output:")
print("The shortest Distance between B and D is", shortest_distance)
print("\n")

# -----------------------------------------
# 3. KRUSKAL'S ALGORITHM
# -----------------------------------------
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
        i, e = 0, 0
        result = []
        parent = []
        rank = []
        self.graph = sorted(self.graph, key=lambda item: item[2])
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        print("Kruskal's Algorithm Output:")
        for u, v, w in result:
            print("%d - %d : %d" % (u, v, w))
        print("\n")

g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal_algo()

# -----------------------------------------
# 4. PRIM'S ALGORITHM
# -----------------------------------------
N = 5
INF = 99999999
selected_node = [False] * N
G = [
    [0, 19, 5, 0, 0],
    [19, 0, 5, 9, 2],
    [5, 5, 0, 1, 6],
    [0, 9, 1, 0, 1],
    [0, 2, 6, 1, 0]
]

selected_node[0] = True
no_edge = 0

print("Prim's Algorithm Output:")
print("Edge : Weight")
while no_edge < N - 1:
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if (not selected_node[n]) and G[m][n]:
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + " - " + str(b) + " : " + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1
print("\n")

# -----------------------------------------
# 5. JOB SCHEDULING
# -----------------------------------------
def job_schedule(jobs):
    jobs.sort(key=lambda x: x[1], reverse=True)
    max_deadline = max(jobs, key=lambda x: x[2])[2]
    slot = [False] * max_deadline
    profit = 0

    for i in range(len(jobs)):
        deadline = jobs[i][2] - 1
        while deadline >= 0 and slot[deadline]:
            deadline -= 1
        if deadline >= 0:
            slot[deadline] = True
            profit += jobs[i][1]
    return profit

jobs = [(1, 50, 2), (2, 10, 1), (3, 20, 2), (4, 30, 1), (5, 40, 3)]
print("Job Scheduling Output:")
print("Maximum Profit:", job_schedule(jobs))
