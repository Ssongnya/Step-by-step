def per(cnt, total):
    global min_cost

    if total > min_cost:
        return

    if cnt == N:
        min_cost = min(min_cost, total)
        return
    
    for i in range(N):
        if used[i]:
            continue

        used[i] = True
        per(cnt + 1, total + cost[i][cnt])
        used[i] = False


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    min_cost = float('inf')

    used = [False for _ in range(N)]

    per(0, 0)

    print(f"#{t} {min_cost}")

    