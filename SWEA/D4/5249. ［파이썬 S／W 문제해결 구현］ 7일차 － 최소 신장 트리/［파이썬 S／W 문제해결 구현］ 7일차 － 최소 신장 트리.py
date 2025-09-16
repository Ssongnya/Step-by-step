class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = []

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))

    # 1. 가중치 기준 정렬
    edges.sort(key=lambda x: x[0])

    ds = DisjointSet(V)
    total_weight = 0
    cnt = 0

    # 2. Kruskal 수행
    for w, u, v in edges:
        if ds.union(u, v):   # 사이클이 안 생기면
            total_weight += w
            cnt += 1
            if cnt == V:     # MST 완성 (간선 개수 = V)
                break

    print(f"#{t} {total_weight}")
