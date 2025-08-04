Test_case = int(input())
for t in range(1, Test_case+1):
    cal = input().split()
    stack = []
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y, #기호에 대한 연산자를 만들어둔다.
    }
    for i in cal: #입력받은 식을 돌려서
        if i == '.': #만약 '.'가 나왔을때
            if len(stack) > 1: #stack이 비어있지 않을때
                result = "error"  #error를 도출하고
            else:
                result = int(stack.pop()) #stack이 비어있지 않으면 정수로 변환 후 pop한것을 결과로 받는다.
        elif i in operators.keys():       #'.'가 나오지 않고 연산자가 ex)'+'.'-' 부분들이 나왔을 때
            if len(stack) < 2:           #만약 stack이 계산할 수 없는 상황일때
                result = "error"         #error를 도출
                break
            else:
                a = int(stack.pop())        #a는 pop한 정수
                b = int(stack.pop())        #b는 pop한 정수
                c = operators[i](int(b), int(a)) #연산자의 i번째를 계산
                stack.append(int(c))            #정수로 변환후 stack에 추가
        else :
            stack.append(i)
    print("#{} {}".format(t, result))