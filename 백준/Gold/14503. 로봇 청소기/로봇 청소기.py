N, M = map(int, input().split())
sx, sy, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]
direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 0

while True:
    if room[sx][sy] == 0:
        room[sx][sy] = -1
        cnt += 1 

    find = False
    for _ in range(4):
        d = (d + 3) % 4
        nx, ny = sx + direct[d][0], sy + direct[d][1]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            sx, sy = nx, ny
            find = True
            break

    if not find:
        r = (d + 2) % 4
        rx, ry = sx + direct[r][0], sy + direct[r][1]

        if 0 <= rx < N and 0 <= ry < M and room[rx][ry] != 1:
            sx, sy = rx, ry
        
        else:
            break

print(cnt)