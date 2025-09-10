def merge_sort(lst):
    global case_num
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    if left[-1] > right[-1]:
        case_num += 1

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    case_num = 0

    fix_nums = merge_sort(nums)

    print(f"#{t} {fix_nums[N//2]} {case_num}")