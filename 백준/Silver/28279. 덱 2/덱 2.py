from collections import deque

N = int(input())
queue = deque()
result = []

for _ in range(N):
    order = input().strip().split()
    if len(order) > 1:
        if order[0] == '1':
            queue.appendleft(int(order[-1]))
            continue
        else:
            queue.append(int(order[-1]))
            continue

    x = int(order[0])

    if x == 3:
        if queue:
            result.append(str(queue.popleft()))
        else:
            result.append('-1')
    elif x == 4:
        if queue:
            result.append(str(queue.pop()))
        else:
            result.append('-1')
    elif x == 5:
        result.append(str(len(queue)))
    elif x == 6:
        result.append('0' if queue else '1')
    elif x == 7:
        result.append(str(queue[0]) if queue else '-1')
    elif x == 8:
        result.append(str(queue[-1]) if queue else '-1')

print('\n'.join(result))
