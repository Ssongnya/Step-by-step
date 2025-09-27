def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x

N = int(input())
M = int(input())

trip = [list(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N+1)]

for i in range(N):
    for j in range(N):
        if trip[i][j] == 1:
            union(i+1, j+1)

where_we_go = list(map(int, input().split()))
start = find(where_we_go[0])

result = True
for k in where_we_go:
    if find(k) != start:
        result = False 
        break

print('YES' if result else 'NO')