T = int(input())

for i in range(1, T + 1):
    N = int(input())
    a_i = list(map(int, input().split()))
    result = max(a_i) - min(a_i)

    print(f'#{i} {result}')
