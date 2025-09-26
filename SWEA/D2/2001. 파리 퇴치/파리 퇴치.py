def catch(x, y, arr):
    n = len(arr)
    hap = 0
    for i in range(x, x + M):
        for j in range(y, y + M):
            hap += arr[i][j]
    return hap
    

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    max_flies = float('-inf')

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            max_flies = max(catch(i, j, flies), max_flies)

    print(f"#{t} {max_flies}")