def safe_zone(arr):
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                count += 1
    return count


def virus_spread(arr):
    stack = virus_lst[:]
    while stack:
        x, y = stack.pop()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = 2
                stack.append((nx, ny))


def wall(arr):
    global max_cnt
    empty = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                empty.append((i, j))

    n = len(empty)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                copy_map = [row[:] for row in my_map]

                x1, y1 = empty[i]
                x2, y2 = empty[j]
                x3, y3 = empty[k]

                copy_map[x1][y1] = 1
                copy_map[x2][y2] = 1
                copy_map[x3][y3] = 1

                virus_spread(copy_map)
                safe = safe_zone(copy_map)

                if safe > max_cnt:
                    max_cnt = safe

def v_lst(arr):
    virus_lst = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                virus_lst.append((i, j))
    return virus_lst


N, M = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(N)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_cnt = -1

virus_lst = v_lst(my_map)

wall(my_map)

print(max_cnt)