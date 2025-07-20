N, M = map(int, input().split())

basket = [0] * (N+1)

for i in range(1, N+1):
    basket[i] = i

for _ in range(M):
    i, j = map(int, input().split())
    before_i = basket[i]
    before_j = basket[j]

    basket[i] = before_j
    basket[j] = before_i   

for n in range(1, N+1) :
    print(basket[n], end=" ")