def binary_search(lst, num):
    left, right = 0 , len(lst) - 1
    direct = 0 # 탐색 방향이 -1 이면 왼쪽 봤던거고 1이면 오른쪽 봤던것임

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == num:
            return True
        
        # 왼쪽
        elif lst[mid] > num:
            curr_dir = -1
            if direct == curr_dir : # 같은 방향을 반복해서 본다면 중단하기
                return False
            right = mid - 1
            direct = curr_dir
        
        # 오른쪽
        else:
            curr_dir = 1
            if direct == curr_dir:
                return False
            left = mid + 1
            direct = curr_dir
    
    return False # 이진탐색을 진행했는데도 값ㄷ을찾지 못하면 False반환

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