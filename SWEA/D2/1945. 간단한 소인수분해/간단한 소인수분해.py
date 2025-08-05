T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    count = [0] * 5
    while N % 2 == 0:
        N /= 2
        count[0] += 1
 
    while N % 3 == 0:
        N /= 3
        count[1] += 1
 
    while N % 5 == 0:
        N /= 5
        count[2] += 1
 
    while N % 7 == 0:
        N /= 7
        count[3] += 1
 
    while N % 11 == 0:
        N /= 11
        count[4] += 1
 
    print(f"#{t} {' '.join(map(str, count))}")