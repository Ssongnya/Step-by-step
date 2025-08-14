T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    for _ in range(M - 1):

        new = list(map(int, input().split()))
        key = new[0]

        idx = len(arr)  # 지금 내 인덱스가 제일 크다고 초기화

        for i, v in enumerate(arr):
            if v > key:
                idx = i
                break

        arr[idx:idx] = new

    result = arr[-10:][::-1]
    print(f"#{t}", *result)