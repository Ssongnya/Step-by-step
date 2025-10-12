M, N = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(M)]

memo = [[0] * N for _ in range(M)]
max_len = 0

for i in range(M):
    for j in range(N):
        if my_map[i][j] == 0:
            if i == 0 or j == 0:
                memo[i][j] = 1
            else:
                memo[i][j] = min(memo[i-1][j-1], memo[i][j-1], memo[i-1][j]) + 1
            max_len = max(max_len, memo[i][j])

print(max_len)