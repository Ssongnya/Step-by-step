T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [[None] * N for _ in range(N)]
    m = N // 2 - 1

    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]

    for j in range(m, m+2):
        for i in range(m, m+2):
            if i == j:
                grid[j][i] = 2

            else:
                grid[j][i] = 1


    for _ in range(M):
        A, B, color = map(int, input().split())
        a, b = A - 1, B - 1     # a가 너가 생각하던 j다
        grid[b][a] = color

        opponent = 1 if color == 2 else 2

        for d in range(8):
            x, y = b + dx[d], a + dy[d]
            flip = []

            if not (0 <= x < N and 0 <= y < N):
                continue

            if grid[x][y] != opponent:
                continue

            while (0 <= x < N and 0 <= y < N and grid[x][y] == opponent):
                flip.append((x, y))
                x += dx[d]
                y += dy[d]

            if 0 <= x < N and 0 <= y < N and grid[x][y] == color and flip:
                for nx, ny in flip:
                    grid[nx][ny] = color

    black = sum(B.count(1) for B in grid)
    white = sum(A.count(2) for A in grid)

    print(f"#{t} {black} {white}")
