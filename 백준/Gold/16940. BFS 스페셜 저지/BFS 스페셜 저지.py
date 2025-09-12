import sys
from collections import deque


def bfs(num):
    global path
    q = deque()
    q.append(num)
    visited[num] = 1

    while q:
        number = q.popleft()
        path.append(number)

        for i in adj_list[number]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


N = int(sys.stdin.readline())
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    node1, node2 = map(int, sys.stdin.readline().split())
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

check = list(map(int, sys.stdin.readline().split()))

rank = [0] * (N + 1)
for idx, v in enumerate(check):
    rank[v] = idx
for v in range(1, N + 1):
    adj_list[v].sort(key=lambda x: rank[x])

visited = [0] * (N + 1)
path = []
bfs(1)

print(1 if path == check else 0)
