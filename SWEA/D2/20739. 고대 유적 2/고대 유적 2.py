T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(N)]

    total = []

    for i in range(N):
        count = 0
        for j in range(M):
            if grid[i][j] == 1 :
                count += 1
            else :
                if count > 1 :
                    total.append(count)
                count = 0
        if count > 1 :
            total.append(count)
    
    for j in range(M):
        count = 0
        for i in range(N):
            if grid[i][j] == 1 :
                count += 1
            else :
                if count > 1 :
                    total.append(count)
                count = 0
        if count > 1 :
            total.append(count)
    
    max_building = 0

    for k in total :
        if k > max_building:
            max_building = k
    
    print(f"#{t} {max_building}")