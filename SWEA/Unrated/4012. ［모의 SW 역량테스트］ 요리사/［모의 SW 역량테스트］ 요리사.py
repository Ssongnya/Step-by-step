def synergy(lst):
    total = 0

    for x in range(len(lst)):
        for y in range(x + 1, len(lst)):
            i = lst[x]
            j = lst[y]
            total += ingredient[i][j] + ingredient[j][i]
    
    return total


def subset(idx, cnt, chosen):
    global min_diff

    if cnt > N // 2 :
        return
    
    if idx >= N:
        if cnt == (N // 2) and len(chosen) == N//2:
            other = [i for i in range(N) if i not in chosen]
            s1 = synergy(chosen)
            s2 = synergy(other)
            diff = abs(s1 - s2)
            min_diff = min(diff, min_diff)
        return

    subset(idx + 1, cnt + 1, chosen + [idx])
    subset(idx + 1, cnt, chosen)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    
    ingredient = [list(map(int, input().split())) for _ in range(N)]

    min_diff = float('inf')

    subset(0, 0, [])

    print(f"#{t} {min_diff}")