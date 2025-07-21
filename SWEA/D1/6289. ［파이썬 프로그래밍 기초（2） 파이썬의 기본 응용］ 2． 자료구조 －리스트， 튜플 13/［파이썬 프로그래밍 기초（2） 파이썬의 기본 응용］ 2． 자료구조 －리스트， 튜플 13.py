num = input()
t_num = tuple(num)

sum_nums = 0

for i in range(len(num)):
    sum_nums += int(t_num[i])

print(sum_nums)