T = int(input())

for t in range(1, T + 1):
    N = int(input())
    count = [0] * 5
    prime_lst = [2, 3, 5, 7, 11]

    for idx, prime in enumerate(prime_lst):
        while N % prime == 0:
            N /= prime
            count[idx] += 1

    print(f"#{t} {' '.join(map(str, count))}")

