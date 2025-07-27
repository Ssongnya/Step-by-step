T = int(input())


for t in range(1, T + 1) :
    N = int(input())
    nums = list(map(int, input().split()))
    print(f'#{t}', end = " ")
    for _ in range(5) :
        max_num = max(nums)
        min_num = min(nums)
        print(max_num, min_num,end = " ")
        nums.pop(nums.index(max_num))
        nums.pop(nums.index(min_num))
    print("")