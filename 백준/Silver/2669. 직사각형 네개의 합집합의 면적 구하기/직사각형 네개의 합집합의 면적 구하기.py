grid = [list(map(int, input().split())) for _ in range(4)]

all = [[0] * 100 for _ in range(100)]

for sx, sy, ex, ey in grid:
    for j in range(sx, ex):
        for k in range(sy, ey):
            all[j][k] += 1

count = 0
for num in all:
    for n in num:
        if n > 0:
            count += 1

print(count)