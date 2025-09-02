T = int(input())

for t in range(1, T + 1):
    N = int(input())

    x, y = 0, 0
    count = 0

    for i in range(-N, N+1):
        for j in range(-N, N+1):
            if (i**2 + j**2) <= N**2:
                count += 1
    print(f"#{t} {count}")
