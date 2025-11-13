N = int(input())

n_lst = list(map(int, input().split()))

M = int(input())

m_lst = list(map(int, input().split()))


n_lst.sort()  # import 없이 가능


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

for m in m_lst:
    if binary_search(n_lst, m):
        print(1)
    else:
        print(0)
