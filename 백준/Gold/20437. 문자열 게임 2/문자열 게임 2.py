T = int(input())

for t in range(T):
    W = input()
    K = int(input())

    alpha = [[] for _ in range(26)]

    for idx, a in enumerate(W):
        alpha[ord(a) - 97].append(idx)

    min_len = float('inf')
    max_len = -1

    for alpha_lst in alpha:
        if len(alpha_lst) < K:
            continue
        
        for j in range(len(alpha_lst) - K + 1):
            start = alpha_lst[j]
            end = alpha_lst[j + K - 1]
            long = end - start + 1

            min_len = min(min_len, long)
            max_len = max(max_len, long)
    if max_len == -1:
        print(-1)
    else:
        print(min_len, max_len)
