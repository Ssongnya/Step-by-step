lst = [12, 24, 35, 70, 88, 120, 155]
del_num = [1, 5, 6]

del_lst = [x for x in lst if (lst.index(x) + 1) not in del_num]
print(del_lst)