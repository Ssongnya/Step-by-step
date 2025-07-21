N, M = map(int, input().split())

basket = [0] * (N + 1)

for i in range(1, N + 1):
    basket[i] = i

for _ in range(M):
    i, j = map(int, input().split())
    rev_basket = basket[i:j+1]
    rev_basket.reverse()
    basket[i:j+1] = rev_basket

for i in range(1, N+1) :
    print(basket[i],end=' ')