from collections import deque


def find_goal():
    queue = deque() # visited 인자 + 거리까지 줘보기
    visited[0][0][0] = True
    queue.append((0, 0, 0, 1))
    while queue:
        x, y, jump, dist = queue.popleft()

        if x == N-1 and y == M-1:
            return dist
        
        for dx, dy in delta:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny][jump] and maze[nx][ny] == 0:
                    visited[nx][ny][jump] = True
                    queue.append((nx, ny, jump, dist + 1))

                elif maze[nx][ny] == 1 and jump == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1, dist + 1))
    
    return -1



N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(N)]
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

result = find_goal()

print(result)