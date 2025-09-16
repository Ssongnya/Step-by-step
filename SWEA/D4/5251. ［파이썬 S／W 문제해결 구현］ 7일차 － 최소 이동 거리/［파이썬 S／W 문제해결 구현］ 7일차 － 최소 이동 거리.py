import heapq


def dijkstra(n, arr):
    inf = float('inf')
    dist = [inf] * (n + 1)
    dist[0] = 0

    pq = [(0, 0)] 

    while pq:
        cost, node = heapq.heappop(pq)
        if cost > dist[node]:
            continue

        for w, e in arr[node]:
            curr = cost + w
            if curr < dist[e]:
                dist[e] = curr
                heapq.heappush(pq, (curr, e))
    return dist[n]



T = int(input())

for t in range(1, T + 1):
    N, E = map(int, input().split())

    graph = {x: [] for x in range(N + 1)}

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))
        
    result = dijkstra(N, graph)
    print(f"#{t} {result}")