from collections import deque


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    apply = list(map(int, input().split()))

    lst = [[] for _ in range(N + 1)]
    applied = [False] * (N + 1)
    cnt = 0

    for i in range(0, 2*M, 2):
        a, b = apply[i], apply[i + 1]
        lst[a].append(b)
        lst[b].append(a)
    
    queue = deque((1, 0))
    cnt = 0

    for i in range(1, N + 1):
        if not applied[i]:
            cnt += 1
            queue = deque([i])
            applied[i] = 1
            while queue:
                now = queue.popleft()
                for nxt in lst[now]:
                    if not applied[nxt]:
                        applied[nxt] = 1
                        queue.append(nxt)
    
    print(f"#{t} {cnt}")

