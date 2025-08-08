T = int(input())

for t in range(1, T + 1):
    N = int(input())
    grid = [[False] * N for _ in range(N)]

    now = 0
    x, y = 0, 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(1, N*N + 1):
        grid[x][y] = i

        nx = x + dx[now]
        ny = y + dy[now]

        if (not 0 <= nx < N) or (not 0 <= ny < N) or grid[nx][ny]:
            now = (now + 1) % 4
            nx, ny = x + dx[now], y + dy[now]

        x, y = nx, ny

    print(f"#{t}")
    for j in grid:
        print(*j)

