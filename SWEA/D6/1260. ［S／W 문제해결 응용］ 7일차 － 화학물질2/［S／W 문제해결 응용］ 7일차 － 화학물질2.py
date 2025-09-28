T = int(input())
for t in range(1, T + 1):
    n = int(input())
    my_map = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    matrix = []

    for i in range(n):
        for j in range(n):
            if my_map[i][j] != 0 and not visited[i][j]:
                garo, sero = 0, 0
                while i + sero < n and my_map[i+sero][j] != 0:
                    sero += 1
                while j + garo < n and my_map[i][j+garo] != 0:
                    garo += 1
                
                for s in range(sero):
                    for g in range(garo):
                        visited[i+s][j+g] = True
                
                matrix.append((sero, garo))
    
    matrix.sort()
    xs = {x: y for (x, y) in matrix}
    ys = [y for (_, y) in matrix]

    start = -1

    for x, y in matrix:
        if x not in ys:
            start = x
            break

    

    direct = [start]
    curr = start

    while curr in xs:
        nxt = xs[curr]
        direct.append(nxt)
        curr = nxt

    m = len(matrix)

    dp = [[0]*(m+1) for _ in range(m+1)]

    for l in range(2, m + 1):
        for k in range(1, m + 2 - l):
            r = k + l - 1
            dp[k][r] = float('inf')
            for x in range(k, r):
                now = dp[k][x] + dp[x+1][r] + direct[k-1]*direct[x]*direct[r]
                dp[k][r] = min(dp[k][r], now)
    
    result = dp[1][m]


    print(f"#{t} {result}")