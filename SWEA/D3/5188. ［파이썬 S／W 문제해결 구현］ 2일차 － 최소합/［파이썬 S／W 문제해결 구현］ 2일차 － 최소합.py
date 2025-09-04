def nums_hap(x, y, prefix):
    global min_hap

    visited[x][y] = True
    prefix += arr[x][y]

    if prefix >= min_hap:
        visited[x][y] = False
        return
    
    if x == (N - 1) and y == (N - 1):
        min_hap = min(min_hap, prefix)
        visited[x][y] = False
        return

    for dx, dy in delta:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            nums_hap(nx, ny, prefix)

    visited[x][y] = False


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    total = 0

    delta = [(1, 0), (0, 1)]

    min_hap = N**2 * 10

    nums_hap(0, 0, 0)

    print(f"#{t} {min_hap}")