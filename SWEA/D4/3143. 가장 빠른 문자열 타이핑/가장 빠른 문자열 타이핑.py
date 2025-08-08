T = int(input())

for t in range(1, T + 1):
    A, B = input().split()

    while (B in A) :
        A = A.replace(B, '1')

    print(f"#{t} {len(A)}")