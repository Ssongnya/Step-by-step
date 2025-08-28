N, K = map(int, input().split())

product = [tuple(map(int, input().split())) for _ in range(N)]

weight = [0] * (K + 1)

for w, v in product:
    for i in range(K, w-1, -1): 
        # weight[K-i] 
        weight[i] = max(weight[i - w] + v, weight[i])

print(weight.pop())