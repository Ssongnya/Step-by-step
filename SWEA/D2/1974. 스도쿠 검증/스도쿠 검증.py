def length(arr):
    for i in range(9):
        lst = {}
        for j in range(9):
            a = arr[i][j]
            if a in lst.keys():
                lst[a] += 1
                return False
            else:
                lst[a] = 1
    return True


def height(arr):
    for j in range(9):
        lst = {}
        for i in range(9):
            a = arr[i][j]
            if a in lst.keys():
                lst[a] += 1
                return False
            else:
                lst[a] = 1
    return True


def nine_nums(arr):
    for k in range(0, 9, 3):
        for c in range(0, 9, 3):
            lst = {}
            for i in range(3):
                for j in range(3):
                    a = arr[i+k][j+k]
                    if a in lst.keys():
                        lst[a] += 1
                        return False
                    else:
                        lst[a] = 1
    return True


T = int(input())

for t in range(1, T+1):
    grid = [[int(x) for x in input().split()] for _ in range(9)]

    if length(grid) and height(grid) and nine_nums(grid):
        print(f"#{t} {1}")

    else :
        print(f"#{t} {0}")