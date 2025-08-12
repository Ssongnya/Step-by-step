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


T = int(input())

for t in range(1, T + 1):
    txt = input()
    s = len(txt)
    stack = [None] * s
    top = -1

    for i in txt:
        if top == -1 or stack[top] != i:
            s_push(i, s)
        else:
            s_pop()

    count = top + 1
    
    print(f"#{t} {count}")