from collections import deque


def find_start(arr, n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                return (i, j)
    return False


def min_distance(arr_s, sx, sy, size, n):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 0

    fish_lst = []
    min_dist = 10000000000000

    while q:
        x, y = q.popleft()

        if visited[x][y] > min_dist:
            break

        for dx, dy in delta:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if arr_s[nx][ny] <= size:
                    visited[nx][ny] = visited[x][y] + 1
            
                    if 0 < arr_s[nx][ny] < size:
                        if visited[nx][ny] <= min_dist:
                            min_dist = visited[nx][ny]
                            fish_lst.append((visited[nx][ny], nx, ny))
                    
                    q.append((nx, ny))

    if fish_lst:
        fish_lst.sort()
        return fish_lst[0]
    
    else:
        return False


N = int(input())

baby_shark = 2

sea = [list(map(int, input().split())) for _ in range(N)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

count = 0
time = 0

start = find_start(sea, N)
sx, sy = start
sea[sx][sy] = 0

while True:
    result = min_distance(sea, sx, sy, baby_shark, N)

    if not result:
        break

    dist, nx, ny = result
    time += dist

    sx, sy = nx, ny

    sea[nx][ny] = 0
    count += 1

    if count == baby_shark:
        baby_shark += 1
        count = 0


print(time)


