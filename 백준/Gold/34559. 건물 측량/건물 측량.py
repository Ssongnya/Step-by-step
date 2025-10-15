import sys
input = sys.stdin.readline


from collections import deque


def can_connect(my_map):
    queue = deque()
    for i in range(N):
        for j in range(M):
            if (i in (0, N-1) or j in (0, M-1)) and my_map[i][j] == 0:
                queue.append((i, j))
                connect[i][j] = True
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not connect[nx][ny] and my_map[nx][ny]==0:
                connect[nx][ny] = True
                queue.append((nx, ny))



N, M = map(int, input().split())
my_map = [list(map(int, input().strip())) for _ in range(N)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
connect = [[False] * M for _ in range(N)]
building = [[0] * M for _ in range(N)]

can_connect(my_map)

for b in range(N):
    for d in range(M):
        if my_map[b][d] == 1 or not connect[b][d]:
            building[b][d] = 1


Q = int(input())

pre = [[0] * (M + 1) for _ in range(N+1)]

for p in range(1, N+1):
    for q in range(1, M+1):
        pre[p][q] = building[p-1][q-1] + pre[p-1][q] + pre[p][q-1] - pre[p-1][q-1]


for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())

    cant_build = pre[x2][y2] - pre[x1-1][y2] - pre[x2][y1-1] + pre[x1-1][y1-1]

    if cant_build == 0:
        print("Yes")
    else:
        print(f"No {cant_build}")


