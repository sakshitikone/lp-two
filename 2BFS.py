from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    traversal = []

    while queue:
        vertex = queue.popleft()
        traversal.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal



v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(v)}

print("Enter edges (u v):")
for _ in range(e):
    u, vtx = map(int, input().split())
    graph[u].append(vtx)
    graph[vtx].append(u)   


start = int(input("Enter starting vertex: "))

result = bfs(graph, start)

print("\nBFS Traversal:")
print(" -> ".join(map(str, result)))