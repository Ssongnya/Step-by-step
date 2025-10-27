from collections import deque

N = int(input())

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

my_map = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
check = [[0] * N for _ in range(N)]

# 한 점과 값(땅에 부여할 값)을 주면 해당 땅에 모두 같은 값을 부여하는 
def connect_island(x, y, value):
    queue = deque([(x, y)])
    check[x][y] = value
    visited[x][y] = True

    while queue:
        qx, qy = queue.popleft()
        for dx, dy in delta:
            nx, ny = qx + dx, qy + dy
            if 0 <= nx < N and 0 <= ny < N and my_map[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                check[nx][ny] = value
                visited[nx][ny] = True


def find_island():
    g_value = 1
    for i in range(N):
        for j in range(N):
            if my_map[i][j] == 1 and not visited[i][j]:
                connect_island(i, j, g_value)
                g_value += 1

find_island()

def bfs(island_num):
    dist = [[-1] * N for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(N):
            if check[i][j] == island_num:
                queue.append((i, j))
                dist[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                # 다른 섬에 도착한 경우
                if check[nx][ny] > 0 and check[nx][ny] != island_num:
                    return dist[x][y]
                # 바다를 확장
                if my_map[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    return float('inf')


# 각 섬마다 BFS 수행
min_bridge = float('inf')
island_count = max(map(max, check))

for num in range(1, island_count + 1):
    min_bridge = min(min_bridge, bfs(num))

print(min_bridge)
