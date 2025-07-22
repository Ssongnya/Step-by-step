lst = [12, 24, 35, 70, 88, 120, 155]

del_lst = [x for x in lst if (lst.index(x) + 1) % 2 == 0]

print(del_lst)