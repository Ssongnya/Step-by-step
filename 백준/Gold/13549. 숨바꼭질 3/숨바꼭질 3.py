from collections import deque

N, K = map(int, input().split())
location = [-1] * 100001
queue = deque()

queue.append(N)
location[N] = 0

while queue:
    x = queue.popleft()
    if x == K:
        print(location[x])
        break
    if 0 <= x * 2 < 100001 and location[x * 2] ==  -1:
        location[x * 2] = location[x]
        queue.append(x * 2)
    
    for next_x in (x-1, x+1):
        if 0 <= next_x < 100001 and location[next_x] == -1:
            location[next_x] = location[x] + 1
            queue.append(next_x)