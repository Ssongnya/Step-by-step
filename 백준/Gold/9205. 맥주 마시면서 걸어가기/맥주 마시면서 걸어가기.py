from collections import deque


def isvalid(x, y, nx, ny):
    dist = abs(nx - x) + abs(ny - y)
    return dist <= 1000


T = int(input())

for t in range(1, T + 1):
    n = int(input())
    stop = [tuple(map(int, input().split())) for _ in range(n+2)]
    
    used = [False] * (n + 2)
    queue = deque([0])

    used[0] = True

    faild = True

    while queue:
        now = queue.popleft()
        if now == n+1:
            faild = False
            break
        for next in range(n+2):
            if not used[next]:
                if isvalid(stop[now][0], stop[now][1], stop[next][0], stop[next][1]):
                    used[next] = True
                    queue.append(next)
        

    result = "happy" if not faild else "sad"

    print(result)