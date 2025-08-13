T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())

        I = i - 1

        for k in range(1, j+1):
            left = I - k
            right = I + k

            if left < 0 and right >= N:
                break

            if left >= 0 and right < N:
                if stones[left] == stones[right]:
                    stones[left] ^= 1
                    stones[right] ^= 1

    print(f"#{t}", *stones)
