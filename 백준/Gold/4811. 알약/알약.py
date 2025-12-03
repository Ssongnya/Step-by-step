dp = [0] * 31
dp[0] = 1

for i in range(1, 31):
    total = 0
    for j in range(i):
        total += dp[j] * dp[i - j - 1]
    dp[i] = total

while True:
    N = int(input())
    if N == 0:
        break
    print(dp[N])