N = int(input())

info = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        if info[j][0] > info[i][0] and info[j][1] > info[i][1]:
            rank += 1
    print(rank, end=" ")