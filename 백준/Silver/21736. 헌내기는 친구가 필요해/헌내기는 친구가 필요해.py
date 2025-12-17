from collections import deque
\
N, M = map(int, input().split())

campus = [input().strip() for _ in range(N)]

def find_i(arr):
    for i in range(N):
        if 'I' in campus[i]:
            j = campus[i].index('I')
            return (i, j)

sx, sy = find_i(campus)
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[False] * M for _ in range(N)]

count = 0
queue = deque([(sx, sy)])
visited[sx][sy] = True
while queue:
    x, y = queue.popleft()

    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and campus[nx][ny] != 'X':
            visited[nx][ny] = True
            if campus[nx][ny] == 'P':
                count += 1
            queue.append((nx, ny))

if not count:
    print('TT')
else:
    print(count)

