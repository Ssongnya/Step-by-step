T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    grid = [[int(x) for x in input().split()] for _ in range(N)]

    hap = []

    for i in range(N):
        count = 0
        for j in range(N):
            if grid[i][j] == 1:
                count += 1
            else :
                hap.append(count)
                count = 0
        hap.append(count)

    for j in range(N):
        count = 0
        for i in range(N):
            if grid[i][j] == 1:
                count += 1
            else:
                hap.append(count)
                count = 0
        hap.append(count)

    hap_count = 0

    for n in hap:
        if n == K:
            hap_count += 1

    print(f"#{t} {hap_count}")