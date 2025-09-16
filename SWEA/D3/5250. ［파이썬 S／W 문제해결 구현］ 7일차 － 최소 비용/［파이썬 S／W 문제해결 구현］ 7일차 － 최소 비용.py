import heapq


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dijkstra(arr):
    inf = float('inf')
    dist = [[inf] * N for _ in range(N)]
    dist[0][0] = 0

    pq = [(0, 0, 0)] # 비용이랑 좌표

    while pq:
        cost, x, y = heapq.heappop(pq)

        if cost > dist[x][y]:
            continue

        
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                basic = 1

                if arr[nx][ny] > arr[x][y]:
                    basic += arr[nx][ny] - arr[x][y]
                
                total = cost + basic

                if total < dist[nx][ny]:
                    dist[nx][ny] = total
                    heapq.heappush(pq, (total, nx, ny))

    return dist[N-1][N-1]


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    my_map = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra(my_map)
    print(f"#{t} {result}")