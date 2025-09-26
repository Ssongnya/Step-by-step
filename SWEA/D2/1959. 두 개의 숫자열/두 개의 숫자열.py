def calc(small, large):

    max_hap = float('-inf')

    s = len(small)
    l = len(large)

    for i in range(l - s + 1):
        hap = 0
        for j in range(s):
            hap += small[j] * large[i + j]
        max_hap = max(hap, max_hap)

    return max_hap

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A_lst = list(map(int, input().split()))
    B_lst = list(map(int, input().split()))

    a = len(A_lst)
    b = len(B_lst)

    if a > b:
        result = calc(B_lst, A_lst)
    else:
        result = calc(A_lst, B_lst)

    print(f"#{t} {result}")