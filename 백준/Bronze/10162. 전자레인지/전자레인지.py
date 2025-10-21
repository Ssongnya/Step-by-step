a = 300
b = 60
c = 10

n = int(input())
result_a = 0
result_c = 0
result_b = 0

while n > 9:
    if n >= a:
        n -= a
        result_a += 1
    elif n >= b:
        n -= b
        result_b += 1
    elif n >= c:
        n -= c
        result_c += 1

if n == 0:
    print(result_a, result_b, result_c)
else:
    print(-1)