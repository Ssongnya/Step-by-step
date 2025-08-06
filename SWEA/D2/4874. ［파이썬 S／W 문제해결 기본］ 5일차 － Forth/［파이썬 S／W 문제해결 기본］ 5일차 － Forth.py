T = int(input())

def evaluate(terms):
    stack = []
    for token in terms.split():
        try :
            stack.append(int(token))
        except ValueError :
            
            if token in ['+', '-', '/', '*'] :
                if len(stack) < 2 :
                    return "error"
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        return "error"
                    stack.append(a // b)
            
            elif token == '.' :
                if len(stack) != 1 :
                    return "error"
                return stack.pop()
            else :
                return "error"
            
    return "error" # 반복이 끝났는데 .이 안나왔다는 뜻

for t in range(1, T + 1):
    terms = input()
    print(f'#{t} {evaluate(terms)}')