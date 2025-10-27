import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_sum = -float('inf')

# row_start ~ row_end 구간 고정
for row_start in range(N):
    tmp = [0] * M  # 열별 누적합

    for row_end in range(row_start, N):
        for col in range(M):
            tmp[col] += arr[row_end][col]

        # Kadane 알고리즘 (1D 최대 부분합)
        current = tmp[0]
        best = tmp[0]
        for i in range(1, M):
            current = max(tmp[i], current + tmp[i])
            best = max(best, current)

        max_sum = max(max_sum, best)

print(max_sum)
