import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

dp[N-1][M-1] = 1

rooms = [(graph[x][y], x, y) for x in range(N) for y in range(M)]
rooms.sort()

for _, x, y in rooms:
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] < graph[x][y]:
            dp[x][y] += dp[nx][ny]
    
print(dp[0][0])