def cantor(num):
    if num == 1:
        return "-"
    side = cantor(num // 3)
    center = " " * (num // 3)    
    return side + center + side

while True:
    try:
        N = int(input())
        print(cantor(3**N))
    except:
        break
