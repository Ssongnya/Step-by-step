lst = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
even_lst = []

for i in range(len(lst)) :
    if lst[i] % 2 == 0 :
        even_lst.append(lst[i])
print(even_lst)