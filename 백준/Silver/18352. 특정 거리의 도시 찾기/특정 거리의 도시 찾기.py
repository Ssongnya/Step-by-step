from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

road = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    road[a].append(b)

visited[X] = 1
queue = deque([X])

while queue:
    now = queue.popleft()
    
    for next in road[now]:
        if visited[next] == 0:
            visited[next] = visited[now] + 1
            queue.append(next)

found = False
for i in range(1, N + 1):
    if visited[i] - 1 == K:
        found = True
        print(i)

if not found:
    print(-1)