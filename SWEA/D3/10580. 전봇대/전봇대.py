T = int(input())

for t in range(1, T + 1):
    N = int(input())
    line = []

    for _ in range(N):
        a, b = map(int, input().split())
        line.append((a, b))
    
    count = 0

    for i in range(N):
        for j in range(i + 1, N):
            lx, ly = line[i]
            dx, dy = line[j]

            if (lx > dx and ly < dy) or (lx < dx and ly > dy):
                count += 1

    print(f"#{t} {count}")