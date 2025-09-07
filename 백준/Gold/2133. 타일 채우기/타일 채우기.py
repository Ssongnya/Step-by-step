N = int(input())

if N % 2 == 1:
    print(0)
    exit()

n = N // 2

cases = [0] * (n + 1)
hap = 0
hap_lst = []

for i in range(n + 1):
    if i == 0:
        cases[i] = 1

    elif i == 1:
         cases[i] = 3
    
    else:
        cases[i] = (cases[i-1] * 3) + (hap_lst[i-2] * 2)
    
    hap += cases[i]
    hap_lst.append(hap)

print(cases[n])