T = int(input())

for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        idx, num = map(int, input().split())
        arr.insert(idx, num)

    print(f"#{t} {arr[L]}")