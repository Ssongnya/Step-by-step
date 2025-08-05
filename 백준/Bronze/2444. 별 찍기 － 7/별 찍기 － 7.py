N = int(input())

for i in range(1, N+1):
    space = ' '*(N-i)
    stars = '*' * (2*i - 1)
    print(space+stars)

for k in range(N-1, 0, -1):
    space = ' '*(N-k)
    stars = '*' * (2*k - 1)
    print(space+stars)