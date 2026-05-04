import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}
    heap = [(0, start)]

    while heap:
        cost, u = heapq.heappop(heap)

        if cost > dist[u]:
            continue

        for v, weight in graph[u]:
            new_cost = dist[u] + weight

            if new_cost < dist[v]:
                dist[v] = new_cost
                prev[v] = u
                heapq.heappush(heap, (new_cost, v))

    return dist, prev


def get_path(prev, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = prev[current]

    return path[::-1]


n = int(input("Enter number of nodes: "))
nodes = []

print("Enter node names:")
for _ in range(n):
    nodes.append(input())

graph = {node: [] for node in nodes}

e = int(input("Enter number of edges: "))

print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = input().split()
    w = int(w)
    graph[u].append((v, w))
    graph[v].append((u, w))

start = input("Enter starting node: ")

dist, prev = dijkstra(graph, start)

print("\nShortest distances from", start, ":")

for node in nodes:
    path = get_path(prev, node)
    print("To", node, ":", dist[node], "Path:", " -> ".join(path))
