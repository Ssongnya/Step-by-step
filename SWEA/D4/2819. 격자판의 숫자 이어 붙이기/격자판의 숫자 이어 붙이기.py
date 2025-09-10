def find_seven(x, y, my_str, cnt):
    if cnt == 7:
        result.add(my_str)
        return
    
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny <4:
            find_seven(nx, ny, my_str + str(arr[nx][ny]), cnt + 1)


T = int(input())

for t in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    result = set()

    delta = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    for i in range(4):
        for j in range(4):
            find_seven(i, j, "", 0)

    print(f"#{t} {len(result)}")
