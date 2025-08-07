def win(x, y):
    if cards[x] == cards[y] :
        return x if x < y else y

    elif (cards[x] == 1 and cards[y] ==3) or \
         (cards[x] == 2 and cards[y] ==1) or \
         (cards[x] == 3 and cards[y] ==2) :
        
        return x
    
    else :
        return y
    
def compete(L, R):
    if L >= R : 
        return L
    
    pivot = (L + R) // 2
    left = compete(L, pivot)
    right = compete(pivot + 1, R)

    return win(left, right)

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))
    winner = compete(1, N)

    print(f"#{t} {winner}")