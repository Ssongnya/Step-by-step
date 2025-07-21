my_mul = []

for i in range(2, 10):
    mul = []
    for k in range(1,10):
        if (i*k % 3 == 0)or (i*k % 7 == 0) :
            continue
        else :
            mul.append(i*k)
    my_mul.append(mul)

print(my_mul)
