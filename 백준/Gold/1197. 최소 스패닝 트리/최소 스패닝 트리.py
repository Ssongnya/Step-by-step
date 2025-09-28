import heapq


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    s, g, w = map(int, input().split())
    graph[s].append((w, g))
    graph[g].append((w, s))

vistied = [False] * (V + 1)

queue = [(0, 1)]
total_cost = 0
count = 0

while queue and count < V:
    cost, now = heapq.heappop(queue)
    if vistied[now]:
        continue
    vistied[now] = True
    total_cost += cost
    count += 1

    for next_cost, next in graph[now]:
        if not vistied[next]:
            heapq.heappush(queue, (next_cost, next))

print(total_cost)