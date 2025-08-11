T = int(input())

def start_point(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return i, j

    return False


def end_point(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3:
                return i, j

    return False

for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    
    sx, sy = start_point(maze)
    ex, ey = end_point(maze)

    visited = [[0]*N for _ in range(N)]
    queue = [(sx, sy)]
    visited[sx][sy] = 1

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    result = 0
    found = False

    while queue:
        x, y = queue.pop(0)  # 맨 앞의 큐 꺼내기

        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
        
            if 0 <= nx < N and 0 <= ny < N :
                if maze[nx][ny] != 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    if maze[nx][ny] == 3 :
                        result = visited[nx][ny] - 2  # 시작점, 도착점 제외
                        found = True
                        break
                    queue.append((nx, ny))
        if found :
            break

    print(f"#{t} {result}")