T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    total = 0

    for i in range(N):
        count = 0
        for j in range(N):
            if grid[i][j] == 1 :
                count += 1
            else :
                if count == K:
                    total += 1
                count = 0
        if count == K :
            total += 1
        
    for j in range(N):
        count = 0
        for i in range(N):
            if grid[i][j] == 1 :
                count += 1
            else :
                if count == K:
                    total += 1
                count = 0
        if count == K :
            total += 1

    print(f"#{t} {total}")
    