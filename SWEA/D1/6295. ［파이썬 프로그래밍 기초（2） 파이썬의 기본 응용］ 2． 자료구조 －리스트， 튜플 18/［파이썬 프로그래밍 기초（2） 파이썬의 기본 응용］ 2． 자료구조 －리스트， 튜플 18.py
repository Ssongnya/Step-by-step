N, M = map(int, input().split(", "))

out_lst = []

for i in range(N) :
    in_lst = []
    for k in range(M) :
        in_lst.append(i*k)
    out_lst.append(in_lst)

print(out_lst)