import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()

for _ in range(N):
    command = list(sys.stdin.readline().split())

    if command[0] == 'push_front':
        q.appendleft(command[1])

    elif command[0] == 'push_back':
        q.append(command[1])

    elif command[0] == 'pop_front':
        if not q:
            print(-1)
        else:
            print(q.popleft())

    elif command[0] == 'pop_back':
        if not q:
            print(-1)
        else:
            print(q.pop())

    elif command[0] == 'size':
        print(len(q))

    elif command[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)

    elif command[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])

    elif command[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
