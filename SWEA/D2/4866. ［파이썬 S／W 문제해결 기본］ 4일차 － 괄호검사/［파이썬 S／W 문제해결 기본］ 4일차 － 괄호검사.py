T = int(input())

for t in range(1, T+1):
    txt = input()
    bracket = []

    for i in txt :
        if i in '{()}' :
            bracket.append(i)
    
    stack = []
    wrong = 0

    for j in bracket :
        if j in "{(" :
            stack.append(j)
        elif j == ")" :
            if stack and stack[-1] == '(': # stack에 아무것도 append 되지 않은 경우 오류가 나므로 stack = True 조건이 들어가줘야한다.!
                stack.pop()
            else :
                wrong += 1
        elif j == "}" :
            if stack and stack[-1] == "{" :
                stack.pop()
            else :
                wrong += 1

    if len(stack)==0 and wrong ==0 :
        result = 1
    else :
        result = 0

    print(f'#{t} {result}')
