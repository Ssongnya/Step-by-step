import heapq

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
reverse = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))
    reverse[v].append((u, t))

def dijkstra(start, goal):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for nxt, w in goal[now]:
            new_cost = cost + w
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))
    return dist

from_X = dijkstra(X, graph)

to_X = dijkstra(X, reverse)

max_time = 0
for i in range(1, N + 1):
    if i == X:
        continue
    max_time = max(max_time, to_X[i] + from_X[i])

print(max_time)
