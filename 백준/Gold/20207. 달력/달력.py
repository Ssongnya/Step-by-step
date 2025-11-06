N = int(input())

days = [0] * 367

for _ in range(N):
    S, E = map(int, input().split())
    for i in range(S, E + 1):
        days[i] += 1

height = 0
width = 0

total = 0

for i in range(1, 367):
    if days[i] > 0:
        width += 1
        height = max(height, days[i])
    
    else:
        if width > 0:
            total += width * height
            width = 0
            height = 0

print(total)