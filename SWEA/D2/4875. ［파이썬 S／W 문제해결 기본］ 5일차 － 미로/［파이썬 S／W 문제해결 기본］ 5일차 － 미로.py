T = int(input())

for t in range(1, T + 1):
    N = int(input())
    maze = [[int(x) for x in input().strip()] for _ in range(N)]

    start_pos = None
    end_pos = None
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_pos = (i, j)
            elif maze[i][j] == 3:
                end_pos = (i, j)

    near = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def backtrack(x, y):
        if (x, y) == end_pos:  # 도착점 도달
            return True

        maze[x][y] = 1  # 방문 표시
        for dx, dy in near:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1:
                if backtrack(nx, ny):
                    return True
        maze[x][y] = 0  # 되돌리기
        return False

    if backtrack(*start_pos):
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")
