# set 사용
# def dupl(lst) :
#     return list(set(lst))

# my_lst = [12,24,35,24,88,120,155,88,120,155]

# print(dupl(my_lst))

nums = [12,24,35,24,88,120,155,88,120,155]
del_nums = []

print([x for x in nums if x not in del_nums and del_nums.append(x) is None])