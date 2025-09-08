def judge(lst):
    if lst[2] < 3:
        return -1
    
    if lst[1] < 2:
        return -1
    
    max2 = lst[2] - 1
    max1 = max2 - 1

    cnt = 0

    if lst[1] > max2:
        cnt += lst[1] - max2
    
    if lst[0] > max1:
        cnt += lst[0] - max1
    
    return cnt

T = int(input())
for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    result = judge(nums)

    print(f"#{t} {result}")