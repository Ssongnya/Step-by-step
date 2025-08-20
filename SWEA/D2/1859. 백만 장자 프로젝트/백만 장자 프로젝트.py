from collections import deque
T = int(input())

for t in range(1, T + 1):
    N = int(input())

    product = list(map(int, input().split()))

    r_pro = deque(reversed(product))

    a = r_pro.popleft()
    earn = 0

    for i in range(len(r_pro)):
        b = r_pro.popleft()
        if a > b:
            earn += a - b
        else:
            a = b

    print(f"#{t} {earn}")