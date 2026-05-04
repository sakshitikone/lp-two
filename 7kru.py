class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


def kruskals_mst(num_vertices, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(num_vertices)
    mst = []

    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            if len(mst) == num_vertices - 1:
                break

    return mst


v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v weight):")
for _ in range(e):
    u, vtx, w = map(int, input().split())
    edges.append((u, vtx, w))


mst = kruskals_mst(v, edges)


print("\nEdges in Minimum Spanning Tree:")
for u, vtx, w in mst:
    print(u, "--", vtx, "weight:", w)
