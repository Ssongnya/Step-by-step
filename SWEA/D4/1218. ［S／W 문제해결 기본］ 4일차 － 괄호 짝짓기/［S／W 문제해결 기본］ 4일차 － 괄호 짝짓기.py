def s_push(item, size):
    global top
    top += 1
    if top == size:
        return False
    else:
        stack[top] = item
        return True


def s_pop():
    global top
    if top == -1:
        return None
    else:
        top -= 1
        return stack[top + 1]


for t in range(1, 11):
    N = int(input())
    bracket = input()
    stack = [None] * N
    top = -1

    result = 1

    pair = {'(': ')', '{': '}', '<': '>', '[': ']'}
    for i in bracket:
        if i in "({[<":
            s_push(i, N)
        else:
            if pair[stack[top]] != i or top == -1:
                result = 0
                break
            else:
                s_pop()

    if top != -1:
        result = 0

    print(f"#{t} {result}")
