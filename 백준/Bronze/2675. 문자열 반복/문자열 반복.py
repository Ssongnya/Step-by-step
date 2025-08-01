T = int(input())

for _ in range(T):
    R, S = map(str, input().split())

    r = int(R)

    for i in S :
        for _ in range(r) :
            print(i, end="")
    
    print('')