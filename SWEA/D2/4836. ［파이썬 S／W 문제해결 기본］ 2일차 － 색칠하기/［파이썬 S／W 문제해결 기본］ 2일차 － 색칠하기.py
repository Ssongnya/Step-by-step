T = int(input())

for case in range(1, T+1) :
    N = int(input())
    grid = [[0]*10 for _ in range(10)]

    for _ in range(N) :
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1) :
            for c in range(c1, c2 + 1) :
                grid[r][c] += 1
    
    purple = 0

    for i in range(10) :
        for j in range(10) :
            if grid[i][j] == 2 :
                purple += 1

    # purple = sum (1 for i in range(10) for j in range(10) if grid[i][j] == 2)

    print(f'#{case} {purple}')