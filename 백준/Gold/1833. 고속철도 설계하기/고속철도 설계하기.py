
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)

    if a != b:
        parent[b] = a

N = int(input())

graph = []

parent = [i for i in range(N + 1)]
total_cost = 0

for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(i+1, N):
        if lst[j] > 0:
            graph.append((lst[j], i+1, j+1))
        else:
            union(i+1, j+1)
            total_cost += abs(lst[j])

graph.sort()

new = []

for cost, s, g in graph:
    if find(s) != find(g):
        union(s, g)
        total_cost += cost
        new.append((s, g))

print(total_cost, len(new))
for x, y in new:
    print(x, y)

