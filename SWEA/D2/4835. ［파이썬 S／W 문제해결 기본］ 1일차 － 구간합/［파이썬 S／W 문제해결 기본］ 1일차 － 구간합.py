T = int(input())

for k in range(1, T + 1) :
    N, M = map(int, input().split())
    a_i = list(map(int, input().split()))

    if len(a_i) != N :
        exit()

    hap = []

    for i in range(N-M+1) : 
        hap_3 = sum(a_i[i:i+M])
        hap.append(hap_3)

    hap_max = max(hap)
    hap_min = min(hap)

    print(f'#{k} {hap_max - hap_min}')