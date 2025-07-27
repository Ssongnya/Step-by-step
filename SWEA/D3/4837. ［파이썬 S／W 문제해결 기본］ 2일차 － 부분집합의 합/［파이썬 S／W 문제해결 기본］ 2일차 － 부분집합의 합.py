T = int(input())

for t in range(1, T + 1) :
    N, K = map(int, input().split())
    total = 0

    for i in range(1<<12) : # 총 원소의 갯수 만큼
        hap = 0
        count = 0

        for k in range(12) :
            if i & (1 << k) : # i에서 k번째 비트가 1인지 검사
                hap += (k + 1)
                count += 1
        
        if count == N and hap == K :
            total += 1
    
    print(f'#{t} {total}')