T = int(input())

for t in range(T):
    N = int(input())
    nums = [0] * (N + 1)
    nums[0] = 1

    for i in range(1, N+1):
        if i == 1:
            nums[i] = 1
        
        elif i == 2:
            nums[i] = 2
        
        else:
            nums[i] = nums[i-3] + nums[i-2] + nums[i-1]
    
    print(nums[N])
