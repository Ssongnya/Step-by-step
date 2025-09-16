class disjointset:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return
        
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    ds = disjointset(N)

    for _ in range(M):
        a, b = map(int, input().split())
        ds.union(a, b)

    roots = set()

    for i in range(1, N + 1):
        roots.add(ds.find(i))
    
    print(f"#{t} {len(roots)}")