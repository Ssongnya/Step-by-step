import heapq

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]   # 인접 리스트
dist = [float('inf')] * (V + 1)      # 최단 거리 배열

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cost, now = heapq.heappop(q)

        if dist[now] < cost:
            continue

        for nxt, w in graph[now]:
            new_cost = cost + w
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))

dijkstra(K)

for i in range(1, V + 1):
    print("INF" if dist[i] == float('inf') else dist[i])