def length(arr):

    max_sum = -1

    for i in range(100):
        len_sum = 0
        for j in range(100):
            len_sum += arr[i][j]
        if len_sum > max_sum:
            max_sum = len_sum

    return max_sum


def height(arr):
    max_sum = -1

    for j in range(100):
        len_sum = 0
        for i in range(100):
            len_sum += arr[i][j]
        if len_sum > max_sum:
            max_sum = len_sum

    return max_sum


def main_cross(arr):
    len_sum = 0

    for i in range(100):
        len_sum += arr[i][i]

    return len_sum


def sub_cross(arr):
    len_sum = 0

    for i in range(100):
        len_sum += arr[i][99-i]

    return len_sum


for t in range(1, 11):

    T = int(input())

    grid = [list(map(int, input().split())) for _ in range(100)]

    max_lst = [length(grid), height(grid), main_cross(grid), sub_cross(grid)]

    result = max_lst[0]

    for num in max_lst:
        if num > result:
            result = num

    print(f"#{T} {result}")
