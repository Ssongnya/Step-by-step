N, M = map(int, input().split())

nums = list(map(int, input().split()))
three_nums = []

max_num = -1
for i in range(N-2):
    for j in range(i + 1, N -1):
        if nums[i] + nums[j] >= M:
            continue
        for k in range(j + 1, N):
            hap = nums[i] + nums[j] + nums[k]
            if hap <= M and hap > max_num:
                max_num = hap
                if max_num == M :
                    print(max_num)
                    exit(0)
print(max_num)