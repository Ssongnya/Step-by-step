T = int(input())

for t in range(1, T + 1):
    N = float(input())

    result = ""

    while 0 < N < 1:
        N *= 2
        if N >= 1:
            result += '1'
            N -= 1
        else:
            result += '0'

        if len(result) > 12:
            result = 'overflow'
            break

    print(f"#{t} {result}")