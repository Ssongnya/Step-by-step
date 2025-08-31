for t in range(1, 11):
    N = int(input())
    fx = input()

    stack = []
    oper = {'+' : 1, '*' : 2}

    result = ''

    for i in fx:
        if i.isnumeric():
            result += i
            continue
        elif not stack:
            stack.append(i)
            continue
        while stack and oper[i] <= oper[stack[-1]]:
            result += stack.pop()
        stack.append(i)
    
    while stack:
        result += stack.pop()
    

    result_stack = []

    for j in result:
        if j.isnumeric():
            result_stack.append(j)
        
        else:
            a = int(result_stack.pop())
            b = int(result_stack.pop())

            if j == "+":
                result_stack.append(a + b)
            else:
                result_stack.append(a * b)



    print(f"#{t} {result_stack[0]}")
                
        