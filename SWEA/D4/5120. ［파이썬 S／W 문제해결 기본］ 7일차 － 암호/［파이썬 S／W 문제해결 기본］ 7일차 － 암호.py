
T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())

    arr = list(map(int, input().split()))
    now = 0

    for _ in range(K):
        
        ins = (now + M) % len(arr) if (now + M) != len(arr) else len(arr)
        
        arr.insert(ins, 0)

        before = (ins - 1) % len(arr)
        after = (ins + 1) % len(arr)

        arr[ins] = arr[before] + arr[after]

        now = ins

    result = arr[::-1][:10]

    print(f"#{t}", *result)