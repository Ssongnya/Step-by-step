import sys
from collections import deque


def sequence(num):
    global first_q
    if len(path) == M:
        first_q.append(path[:])
        return

    for i in range(num, len(put_virus)):
        path.append(put_virus[i])
        sequence(i + 1)
        path.pop()


N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

circuit_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]
put_virus = []
path = []

for row in range(N):
    for column in range(N):
        if lab[row][column] == 2:
            put_virus.append([row, column])

first_q = deque()
sequence(0)

count = float('inf')
check_q = deque()
while first_q:
    middle_q = first_q.popleft()

    visited = [[-1] * N for _ in range(N)]
    check_q = deque()

    for x, y in middle_q:
        visited[x][y] = 0
        check_q.append((x, y))

    while check_q:
        x, y = check_q.popleft()

        for row, col in circuit_list:
            new_row, new_col = x + row, y + col
            if 0 <= new_row < N and 0 <= new_col < N:
                if lab[new_row][new_col] != 1 and visited[new_row][new_col] == -1:
                    visited[new_row][new_col] = visited[x][y] + 1
                    check_q.append((new_row, new_col))

    time_max = 0
    ok = True
    for r in range(N):
        for c in range(N):
            if lab[r][c] == 0 or lab[r][c] == 2:
                if visited[r][c] == -1:
                    ok = False
                    break
                time_max = max(time_max, visited[r][c])

        if not ok:
            break

    if ok:
        count = min(count, time_max)

print(-1 if count == float('inf') else count)