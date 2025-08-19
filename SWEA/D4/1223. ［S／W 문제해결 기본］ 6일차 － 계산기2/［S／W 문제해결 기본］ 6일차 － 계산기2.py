def postfix(my_str):
    priority = {'+': 1, '*': 2}
    stack = []

    fix = ""

    for s in my_str:
        if s.isdigit():
            fix += s
        else:
            while stack and priority[stack[-1]] >= priority[s]:
                fix += stack.pop()
            stack.append(s)
    
    while stack:
        fix += stack.pop()

    return fix



for t in range(1, 11):
    N = int(input())
    fx = input()

    fixed = postfix(fx)

    stack = []

    for i in fixed:
        if i.isdigit():
            stack.append(int(i))

        else:
            b = stack.pop()
            a = stack.pop()

            if i == "+":
                stack.append(a + b)
            else:
                stack.append(a*b)
    print(f"#{t} {stack[0]}")