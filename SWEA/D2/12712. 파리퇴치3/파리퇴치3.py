def plus_catch(x, y):
    global max_kill
    kill = grid[x][y]
    for i, j in plus_line:
        for m in range(1, M):
            px, py = x + m * i, y + m * j
            if 0<= px <N and 0<= py <N:
                kill += grid[px][py]
    if kill > max_kill :
        max_kill = kill

def cross_catch(x, y):
    global max_kill
    kill = grid[x][y]
    for i, j in cross_line:
        for m in range(1, M):
            px, py = x + m * i, y + m * j
            if 0<= px <N and 0<= py <N:
                kill += grid[px][py]
    if kill > max_kill :
        max_kill = kill

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    plus_line = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cross_line = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    max_kill = -1

    for i in range(N):
        for j in range(N):
            plus_catch(i, j)
            cross_catch(i, j)

    print(f"#{t} {max_kill}")

