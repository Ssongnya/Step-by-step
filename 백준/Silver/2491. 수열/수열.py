def increase(lst, n):
    count = 0
    count_lst = []
    for i in range(1, n):
        if lst[i] >= lst[i-1]:
            count += 1
        else :
            count_lst.append(count)
            count = 0
    count_lst.append(count)
    
    return max(count_lst) + 1

def decrease(lst, n):
    count = 0
    count_lst = []
    for i in range(1, n):
        if lst[i] <= lst[i-1]:
            count += 1
        else :
            count_lst.append(count)
            count = 0
    count_lst.append(count)
    return max(count_lst) + 1

N = int(input())
num_lst = list(map(int, input().split()))

result = max(increase(num_lst, N), decrease(num_lst, N))

print(result)