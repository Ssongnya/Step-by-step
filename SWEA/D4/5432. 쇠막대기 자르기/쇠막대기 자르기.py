T = int(input())

for t in range(1, T + 1):

    text = input()
    change = text.replace("()", "1")

    open_b = 0
    pieces = 0

    for i in change :
        if i == "(":
            open_b += 1
        
        elif i == ")" :
            open_b -= 1
            pieces  += 1 # 마지막 끝 피스
        
        else :
            pieces += open_b

    print(f"#{t} {pieces}")