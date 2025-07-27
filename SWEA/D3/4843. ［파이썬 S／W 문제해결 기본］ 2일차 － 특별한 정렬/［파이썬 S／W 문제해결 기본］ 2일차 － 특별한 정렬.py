T = int(input())

for t in range(1, T + 1) :
    N = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    result = []

    left = 0
    right = N - 1

    for i in range(10) :
        if i % 2 == 0 :
            result.append(nums[right])
            right -= 1

        else :
            result.append(nums[left])
            left += 1

    print(f'#{t}', *result)