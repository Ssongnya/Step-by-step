T = int(input())

for t in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    stock = stock[::-1]
    total = 0
    max_stock = stock[0]

    for i in stock:
        if i < max_stock:
            total += max_stock - i

        max_stock = max(max_stock, i)

    print(total)