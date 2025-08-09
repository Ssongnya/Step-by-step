T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))
    for m in range(M):
        i, j = map(int, input().split())
        
        I = i - 1

        for k in range(1, j + 1):
            left = I - k
            right = I + k

            if left < 0 or right >= N :
                break

            if stones[left] == stones[right]:
                stones[left] = 1 - stones[left]
                stones[right] = 1 - stones[right]
    
    print(f"#{t}", *stones)


    