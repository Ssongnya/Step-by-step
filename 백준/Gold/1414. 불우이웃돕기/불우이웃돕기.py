def convert(alpha):
    if alpha == '0':
        return 0
    elif 'a' <= alpha <= 'z':
        return ord(alpha) - ord('a') + 1
    else:
        return ord(alpha) - ord('A') + 27
    

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N = int(input())
direct = []
hap = 0

graph = [input().strip() for _ in range(N)]

for i in range(N):
    for j in range(N):
        cost = convert(graph[i][j])
        hap += cost
        if i == j or cost == 0:
            continue
        direct.append((cost, i, j))

direct.sort(key = lambda x: x[0])
parent = [i for i in range(N)]

min_cost = 0
count = 0

for cost, x, y in direct:
    if find(x) != find(y):
        union(x, y)
        min_cost += cost
        count += 1
        if count == N - 1:
            break

if count != N - 1:
    print(-1)
else:
    print(hap - min_cost)
