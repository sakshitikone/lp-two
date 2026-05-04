import heapq

def prims_mst(graph, start=0):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    min_heap = [(0, start, -1)]
    mst = []
    total_cost = 0

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total_cost += weight

        if parent != -1:
            mst.append((parent, u, weight))

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return mst, total_cost

v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(v)}

print("Enter edges (u v weight):")
for _ in range(e):
    u, vtx, w = map(int, input().split())
    graph[u].append((vtx, w))
    graph[vtx].append((u, w))   


start = int(input("Enter starting vertex: "))
mst, cost = prims_mst(graph, start)


print("\nPrim's MST Edges:")
for u, vtx, w in mst:
    print(u, "--", vtx, "weight:", w)

print("Total Cost:", cost)
