N = int(input())

points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((y, x))

points.sort()

for y, x in points:
    print(x, y)