T = int(input())

for t in range(1, T + 1) :
    N = input()
    M = input()

    n = len(N)
    m = len(M)

    result = 0

    for i in range(m - n + 1) :
        if M[i:i+n] == N :
            result += 1
            break
        
        else :
            continue

    if result == 1 :
        print(f'#{t}', 1)
    else :
        print(f'#{t}', 0)