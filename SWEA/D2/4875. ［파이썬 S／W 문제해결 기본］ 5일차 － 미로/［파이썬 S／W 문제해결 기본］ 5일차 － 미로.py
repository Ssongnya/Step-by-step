from collections import deque

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    maze = [[int(x) for x in input().strip()] for _ in range(N)]

    start_pos = end_pos = None
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_pos = (i, j)
            elif maze[i][j] == 3:
                end_pos = (i, j)

    visited = [[0] * N for _ in range(N)]
    queue = deque([start_pos])
    visited[start_pos[0]][start_pos[1]] = 1
    found = False

    while queue:
        x, y = queue.popleft()

        if (x, y) == end_pos:  # 도착점 발견
            found = True
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))

    print(f"#{t} {1 if found else 0}")
