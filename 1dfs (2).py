def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()

    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(v)}

print("Enter edges (u v):")
for _ in range(e):
    u, vtx = map(int, input().split())
    graph[u].append(vtx)
    graph[vtx].append(u)   


start = int(input("Enter starting vertex: "))

print("\nDFS Traversal:")
dfs(graph, start)
print()
