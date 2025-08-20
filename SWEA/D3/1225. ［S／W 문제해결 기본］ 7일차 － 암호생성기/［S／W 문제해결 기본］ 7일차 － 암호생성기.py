from collections import deque


for _ in range(1, 11):
    t = int(input())

    nums = deque(list(map(int, input().split())))

    i = 1
    while True:

        a = nums.popleft() - i
        if a <= 0:
            nums.append(0)
            break
        else:
            nums.append(a)
        i += 1
        if i > 5:
            i = 1

    print(f"#{t}", *nums)