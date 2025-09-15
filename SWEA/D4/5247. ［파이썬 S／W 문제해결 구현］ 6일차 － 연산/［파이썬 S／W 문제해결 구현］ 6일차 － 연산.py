from collections import deque


def calc(num):
    return [num + 1, num - 1, num * 2, num - 10]


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    queue = deque([(N, 0)])

    checked = [False] * 1000001
    checked[N] = True

    result = 0

    while queue:
        now, cnt = queue.popleft()
        
        if now == M:
            result = cnt
            break

        for nxt in calc(now):
            if 1 <= nxt <= 1000000 and not checked[nxt]:
                checked[nxt] = True
                queue.append((nxt, cnt + 1))
        
    print(f"#{t} {result}")