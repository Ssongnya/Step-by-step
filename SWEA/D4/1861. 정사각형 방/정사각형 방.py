
T = int(input())
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]

    dp[x][y] = 1  # 최소 자기 자신 포함
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if rooms[nx][ny] == rooms[x][y] + 1:
                dp[x][y] = max(dp[x][y], 1 + dfs(nx, ny))
    return dp[x][y]

for t in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*N for _ in range(N)]

    max_len = 0
    start_num = N*N + 1

    for i in range(N):
        for j in range(N):
            length = dfs(i, j)
            if length > max_len:
                max_len = length
                start_num = rooms[i][j]
            elif length == max_len and rooms[i][j] < start_num:
                start_num = rooms[i][j]

    print(f"#{t} {start_num} {max_len}")
