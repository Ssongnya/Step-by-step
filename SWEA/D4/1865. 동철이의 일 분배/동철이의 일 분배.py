def permu(idx, percent):

    global max_per

    if percent <= max_per:
        return
    
    if idx == N:
        max_per = max(max_per, percent)
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = True
            permu(idx + 1, percent * (P[i][idx] * 0.01))
            used[i] = False


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    used = [False] * N

    max_per = -1
    permu(0, 1)

    print(f"#{t} {max_per*100 :.6f}")
