T = int(input())

def monster(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return i, j
    return None


def attack(arr, x, y):
    n = len(arr)

    safe = 0

    wall = False
    for k in range(y-1, -1, -1):
        if not wall:    # 벽이 아직 없었다면
            if arr[x][k] == 1:
                wall = True
        else :      # 벽을 만났다면
            if arr[x][k] == 0 :
                safe += 1

    wall = False
    for k in range(y+1, n):
        if not wall:
            if arr[x][k] == 1:
                wall = True
        else :
            if arr[x][k] == 0 :
                safe += 1

    wall = False
    for k in range(x-1, -1, -1):
        if not wall:    # 벽이 아직 없었다면
            if arr[k][y] == 1:
                wall = True
        else :      # 벽을 만났다면
            if arr[k][y] == 0 :
                safe += 1

    wall = False
    for k in range(x+1, n):
        if not wall:
            if arr[k][y] == 1:
                wall = True
        else :
            if arr[k][y] == 0 :
                safe += 1

    return safe
    
     

for t in range(1, T + 1):
    N = int(input())

    grid = [list(map(int, input().split())) for _ in range(N)]

    x, y = monster(grid)

    count = 0

    for i in range(N):
        for j in range(N):
            if i != x and j != y and grid[i][j] == 0:
                count += 1

    result = count + attack(grid, x, y)

    print(f"#{t} {result}")

