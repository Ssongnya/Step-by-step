T = int(input())

for t in range(1, T+1):

    N = int(input())
    num_lst = list(map(int, input().split()))

    max_num = num_lst[0]
    min_num = num_lst[0]

    for x in num_lst:
        if x > max_num:
            max_num = x
    for n in num_lst:
        if n < min_num:
            min_num = n
    print(f'#{t} {max_num - min_num}')