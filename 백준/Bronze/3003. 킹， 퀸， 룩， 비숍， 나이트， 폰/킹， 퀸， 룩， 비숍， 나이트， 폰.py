now = list(map(int, input().split()))

origin = [1, 1, 2, 2, 2, 8]

for idx, value in enumerate(now) :
    print(origin[idx]-value, end=" ")