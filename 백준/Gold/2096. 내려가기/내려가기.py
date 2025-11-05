N = int(input())

max_lst = [0]*3
min_lst = [0]*3

for _ in range(N):
    my_max = max_lst[:]
    my_min = min_lst[:]

    n1, n2, n3 = map(int, input().split())
    max_lst[0] = n1 + max(my_max[0], my_max[1])
    max_lst[1] = n2 + max(my_max[0], my_max[1], my_max[2])
    max_lst[2] = n3 + max(my_max[1], my_max[2])

    min_lst[0] = n1 + min(my_min[0], my_min[1])
    min_lst[1] = n2 + min(my_min[0], my_min[1], my_min[2])
    min_lst[2] = n3 + min(my_min[1], my_min[2])

print(max(max_lst), min(min_lst))