T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    sum_lst = []
    for i in range(N - M + 1):
        hap = 0
        for k in range(i, i + M):
            hap += ai[k]
        sum_lst.append(hap)

    max_sum = sum_lst[0]
    min_sum = sum_lst[0]

    for num in sum_lst:
        if num > max_sum:
            max_sum = num
        if num < min_sum:
            min_sum = num

    print(f'#{t} {max_sum - min_sum}')