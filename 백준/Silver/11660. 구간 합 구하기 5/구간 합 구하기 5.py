import sys
input = sys.stdin.readline

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

pf_sum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        pf_sum[i][j] = table[i-1][j-1] + pf_sum[i-1][j] + pf_sum[i][j-1] - pf_sum[i-1][j-1]

for m in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    result = pf_sum[x2][y2] - pf_sum[x1-1][y2] - pf_sum[x2][y1-1] + pf_sum[x1-1][y1-1]

    print(result)