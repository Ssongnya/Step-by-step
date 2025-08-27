N = int(input())

count = 0
solve = False

while N >= 0:
    if N % 5 == 0:
        count += N // 5
        print(count)
        solve = True
        break
    N -= 3
    count += 1

if not solve:
    print(-1)

