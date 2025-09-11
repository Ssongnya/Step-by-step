def move(x, y, cnt, s):
    global max_count, start

    if cnt > max_count or (cnt == max_count and s < start):
        max_count = cnt
        start = s


    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and nums[x][y] + 1 == nums[nx][ny]:
            move(nx, ny, cnt + 1, s)

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    max_count = 0
    start = float('inf')

    for i in range(N):
        for j in range(N):
            move(i, j, 1, nums[i][j])

    print(f"#{t} {start} {max_count}")