T = int(input())

def fact(num):

    result = 1

    for i in range(1, num + 1):
        result *= i
    
    return result


for _ in range(T):
    big = -1
    small = -1

    a, b = map(int, input().split())

    big = a if a > b else b
    small = b if a > b else a

    answer = (fact(big) // fact(big - small)) // fact(small)

    print(answer)
 