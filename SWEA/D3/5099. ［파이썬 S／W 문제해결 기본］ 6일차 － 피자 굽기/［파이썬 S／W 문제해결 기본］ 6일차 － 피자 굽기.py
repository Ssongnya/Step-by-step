from collections import deque

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    cheese_lst = list(map(int, input().split()))

    oven = deque()

    pizza = deque((i + 1, cheese_lst[i]) for i in range(M))

    for _ in range(N):
        oven.append(pizza.popleft())
    
    while len(oven) > 1:
        pizza_num, cheese = oven.popleft()
        cheese //= 2

        if cheese > 0:
            oven.append((pizza_num, cheese))
        else:
            if pizza:
                oven.append(pizza.popleft())

    last_pizza = oven[0][0]
    print(f"#{t} {last_pizza}")