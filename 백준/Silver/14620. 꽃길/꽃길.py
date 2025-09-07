def isvaild(x, y):
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        if visited[nx][ny]:
            return False
    return True


def price_hap(x, y):
    hap = 0
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        hap += price[nx][ny]
    return hap


def find_min(now_hap, cnt): 
    global min_hap

    if cnt >= 3:
        min_hap = min(min_hap, now_hap)
        return

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if isvaild(i, j):
                for dx, dy in delta:
                    nx = i + dx
                    ny = j + dy
                    visited[nx][ny] = True
                find_min(now_hap + price_hap(i, j), cnt + 1)
                for dx, dy in delta:
                    nx = i + dx
                    ny = j + dy
                    visited[nx][ny] = False



N = int(input())

price = [list(map(int, input().split())) for _ in range(N)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
visited = [[False] * N for _ in range(N)]
min_hap = 1000000000000000000000

find_min(0, 0)

print(min_hap)