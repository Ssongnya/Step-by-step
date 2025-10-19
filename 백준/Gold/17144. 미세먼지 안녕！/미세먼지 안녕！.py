
R, C, T = map(int, input().split())

cleaner = []

dust_map = [list(map(int, input().split())) for _ in range(R)]

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(R):
    if dust_map[i][0] == -1:
        cleaner.append((i, 0))


def spread():
    spread_arr = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if dust_map[i][j] > 0:
                sep = dust_map[i][j] // 5
                count = 0

                for dx, dy in delta:
                    nx, ny = i + dx, j + dy

                    if 0 <= nx < R and 0 <= ny < C and dust_map[nx][ny] != -1:
                        spread_arr[nx][ny] += sep
                        count += 1
                dust_map[i][j] -= sep * count

    for i in range(R):
        for j in range(C):
            dust_map[i][j] += spread_arr[i][j]


def clean():
    high, low = cleaner

    ux, uy = high

    for x in range(ux - 1, 0, -1):
        dust_map[x][0] = dust_map[x - 1][0]
    
    for y in range(C - 1):
        dust_map[0][y] = dust_map[0][y + 1]

    for x in range(ux):
        dust_map[x][C - 1] = dust_map[x + 1][C - 1]

    for y in range(C - 1, 1, -1):
        dust_map[ux][y] = dust_map[ux][y - 1]

    dust_map[ux][1] = 0

    lx, ly = low

    for x in range(lx + 1, R - 1):
        dust_map[x][0] = dust_map[x + 1][0]

    for y in range(C - 1):
        dust_map[R - 1][y] = dust_map[R - 1][y + 1]

    for x in range(R - 1, lx, -1):
        dust_map[x][C - 1] = dust_map[x - 1][C - 1]

    for y in range(C - 1, 1, -1):
        dust_map[lx][y] = dust_map[lx][y - 1]

    dust_map[lx][1] = 0


for _ in range(T):
    spread()
    clean()

result = 0

for i in range(R):
    for j in range(C):
        if dust_map[i][j] > 0:
            result += dust_map[i][j]

print(result)