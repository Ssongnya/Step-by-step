def fact(num):
    n = 1
    for i in range(1, num+1):
        n *= i
    return n


my_num = fact(int(input()))

my_str = str(my_num)

count = 0
str_len = len(my_str)
for i in range(str_len - 1, -1, -1):
    if my_str[i] == '0':
        count += 1
    elif count > 0 and my_str[i] != '0':
        break


print(count)