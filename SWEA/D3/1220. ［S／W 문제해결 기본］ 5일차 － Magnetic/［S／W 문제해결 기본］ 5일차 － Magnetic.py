def to_s(x, y):
    while x < N - 1:
        nx = x + 1
        ny = y
        if arr[nx][ny] == 1:
            return False
        elif arr[nx][ny] == 2:
            return True
        x = nx
    else:
        return False

for t in range(1, 11):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                if to_s(i, j):
                    count += 1
    print(f"#{t} {count}")