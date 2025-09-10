def binary_search(lst, num):
    left, right = 0 , len(lst) - 1
    direct = 0

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == num:
            return True
        elif lst[mid] > num:
            curr_dir = -1
            if direct == curr_dir :
                return False
            right = mid - 1
            direct = curr_dir
        else:
            curr_dir = 1
            if direct == curr_dir:
                return False
            left = mid + 1
            direct = curr_dir
    
    return False


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    A.sort()

    B = list(map(int, input().split()))

    count = 0

    for n in B:
        if binary_search(A, n):
            count += 1

    print(f"#{t} {count}")