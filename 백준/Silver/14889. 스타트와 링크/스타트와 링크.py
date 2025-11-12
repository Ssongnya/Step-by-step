def ability(lst):
    total = 0
    for i in lst:
        for j in lst:
            if i == j:
                continue
            total += board[i][j]
    return total


def subset(idx, chosen, c, other, o):

    global min_diff

    if idx >= N:
        if c == N//2 and o == N//2:
            min_diff = min(min_diff, abs(ability(chosen) - ability(other)))
        return

    if c > N // 2 or o > N // 2:
        return
    
    subset(idx + 1, chosen + [idx], c + 1, other, o)
    subset(idx + 1, chosen, c, other + [idx], o + 1)


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
min_diff = float('inf')

subset(0, [], 0, [], 0)
print(min_diff)