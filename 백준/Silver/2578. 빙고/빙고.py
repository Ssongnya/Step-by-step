grid = [list(map(int, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]

def find_bingo(arr, num):
    found = False
    bingo = 0
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                visited[i][j] = True
                found = True
                break
        if found:
            break

    for x in range(5):
        if all(visited[x][y] for y in range(5)):
            bingo += 1

    for y in range(5):
        if all(visited[x][y] for x in range(5)):
            bingo += 1
    
    if all(visited[x][x] for x in range(5)):
        bingo += 1

    if all(visited[x][4-x] for x in range(5)):
        bingo += 1

    return bingo

call_num = [list(map(int, input().split())) for _ in range(5)]

result = 0
for i in range(5):
    for j in range(5):
        if find_bingo(grid, call_num[i][j]) >= 3:
            result = i * 5 + j + 1
            break
    if result:
        break

print(result)
        