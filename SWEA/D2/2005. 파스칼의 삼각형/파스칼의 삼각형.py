T = int(input())

for t in range(1, T + 1):

    N = int(input())

    if N == 1:
        print(f"#{t}")
        print(1)
        continue

    nums = [[0]*(i + 1) for i in range(N)]

    for j in range(N):
        nums[j][0] = nums[j][j] = 1

        for k in range(1, j):
            nums[j][k] = nums[j-1][k-1] + nums[j-1][k]

    print(f"#{t}")
    for n in nums:
        print(*n)
