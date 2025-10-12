def bomb(arr):
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1), (0, 0)]
    visited = [[False]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if arr[x][y] != 'O':
                continue
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    visited[nx][ny] = True
    
    new_map = [['O']*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if visited[i][j]:
                new_map[i][j] = '.'

    return new_map


import copy
R, C, N = map(int, input().split())

bombs = [list(input().strip()) for _ in range(R)]

result = [[] for _ in range(3)]

result[0] = copy.deepcopy(bombs)
result[1] = [['O']*C for _ in range(R)]
result[2] = bomb(result[0])

if N == 1:
    ans = result[0]
elif N % 2 == 0:
    ans = result[1]
elif N % 4 == 3:
    ans = result[2]
else:
    ans = bomb(result[2])

for row in ans:
    print("".join(row))