T = int(input())

for t in range(1, T + 1):
    N = int(input())
    corridor = [0] * 201

    for _ in range(N):
        a, b = map(int, input().split())
        end = a if a > b else b
        start = b if b < a else a

        start = (start + 1) // 2
        end = (end + 1) // 2

        for i in range(start, end + 1):
            corridor[i] += 1
        
    print(f"#{t} {max(corridor)}")