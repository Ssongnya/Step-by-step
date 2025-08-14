T = int(input())

for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    for _ in range(M):
        order = list(input().split())

        if order[0] == "I":
            idx = int(order[1])
            num = int(order[2])
            nums.insert(idx, num)
        
        elif order[0] == "D":
            idx = int(order[1])
            nums.pop(idx)
        
        elif order[0] == "C":
            idx = int(order[1])
            num = int(order[2])
            nums[idx] = num
    
    result = nums[L] if 0 <= L < len(nums) else -1
    print(f"#{t} {result}")