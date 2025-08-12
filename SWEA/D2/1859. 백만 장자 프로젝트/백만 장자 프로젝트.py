T = int(input())

for t in range(1, T + 1):
    day = int(input())
    price = list(map(int, input().split()))

    stack = []
    earn = 0

    for i in range(day-1, -1, -1):
        if not stack or price[i] > stack[-1]:
            stack.append(price[i])

        else:
            earn += stack[-1] - price[i]

    print(f"#{t} {earn}")