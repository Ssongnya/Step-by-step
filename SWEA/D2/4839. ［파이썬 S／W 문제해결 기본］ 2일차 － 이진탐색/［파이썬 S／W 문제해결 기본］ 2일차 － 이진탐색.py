T = int(input())

# 이진 탐색 함수 만들기

def binary(page, want) :
    l = 1
    r = page
    count = 0

    while l <= r :
        
        count += 1

        c = l + (r - l) // 2

        if want == c :
            return count
        elif want < c :
            r = c
        else :
            l = c

    return count
    


for t in range(1, T + 1) :
    P, Pa, Pb = map(int, input().split())
    
    count_a = binary(P, Pa)
    count_b = binary(P, Pb)
    
    if count_a > count_b :
        winner = 'B'
    elif count_a == count_b :
        winner = 0
    else :
        winner = 'A'

    print(f'#{t} {winner}')