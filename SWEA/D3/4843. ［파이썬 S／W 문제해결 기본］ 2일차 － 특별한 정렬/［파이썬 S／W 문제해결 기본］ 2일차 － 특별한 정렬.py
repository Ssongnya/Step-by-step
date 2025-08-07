T = int(input())


def find_max(lst):
    global nums
    max_num = -1
    max_idx = -1
    for n in range(len(lst)):
        if lst[n] > max_num:
            max_num = lst[n]
            max_idx = n
    nums.pop(max_idx)
    return max_num


def find_min(lst):
    global nums
    min_num = 100000000
    min_idx = -1
    for n in range(len(lst)):
        if lst[n] < min_num:
            min_num = lst[n]
            min_idx = n
    nums.pop(min_idx)
    return min_num


for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    print(f"#{t}", end=" ")
    for i in range(10):
        if i % 2 == 0:
            print(find_max(nums), end=" ")
        else:
            print(find_min(nums), end=" ")
    print("")
