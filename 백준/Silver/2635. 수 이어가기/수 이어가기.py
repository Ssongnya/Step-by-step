N = int(input())

max_len = -1
result = []

for i in range(1, N + 1):    # N 포함
    num_lst = [N]

    num_lst.append(i)
    n = 2
    while num_lst[n-2] - num_lst[n-1] >= 0:
        num_lst.append(num_lst[n-2] - num_lst[n-1])
        n += 1
    if len(num_lst) > max_len:
        max_len = len(num_lst)
        result = num_lst[:]    # 리스트 안전하게 복사

print(max_len)
print(*result)