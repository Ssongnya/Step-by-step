T = int(input())


def find_min(lst):
    global sort_lst

    while len(lst) > 0:

        min_num = 10000000000000
        min_idx = -1

        for i in range(len(lst)):
            if lst[i] < min_num:
                min_num = lst[i]
                min_idx = i

        sort_lst.append(min_num)
        lst.pop(min_idx)


for t in range(1, T + 1):
    N = int(input())

    num_lst = list(map(int, input().split()))

    sort_lst = []

    find_min(num_lst)

    print(f"#{t}", *sort_lst)
