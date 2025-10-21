def Prime_num_list(n):
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    i = 2
    while i * i <= n:  
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        i += 1
    
    return [i for i in range(2, n + 1) if is_prime[i]]

n = int(input())
sum_list = Prime_num_list(n)


if n in sum_list:
    result = 1
    sum_list.pop()
    i = len(sum_list)-1
    j = i
    sum_num = 0
else:
    result = 0
    i = len(sum_list)
    j = i
    sum_num = 0

while i >= 0:
    if sum(sum_list[i:j+1]) < n:
        i -= 1
    elif sum(sum_list[i:j+1]) > n:
        j -= 1
        i = j
    elif sum(sum_list[i:j+1]) == n:
        j -= 1
        i = j
        result += 1

print(result)