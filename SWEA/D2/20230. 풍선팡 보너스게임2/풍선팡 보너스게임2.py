T = int(input())

for t in range(1, T + 1):
    N = int(input())

    grid = [list(map(int, input().split())) for _ in range(N)]

    row_sum = [0] * N

    for i in range(N):
        total = 0
        for j in range(N):
            total += grid[i][j]
        row_sum[i] = total
    
    
    col_sum = [0] * N
    
    for j in range(N):
        total = 0
        for i in range(N):
            total += grid[i][j]
        col_sum[j] = total


    max_sum = -1

    for i in range(N):
        for j in range(N):
            score = row_sum[i] + col_sum[j] - grid[i][j]
            if score > max_sum:
                max_sum = score
    
    print(f"#{t} {max_sum}")
