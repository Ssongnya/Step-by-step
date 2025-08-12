T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())

    near = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        near[a].append(b)
        near[b].append(a)

    S, G = map(int, input().split())

    visited = [-1] * (V + 1)
    queue = [S]
    front = 0
    visited[S] = 0  # 방문처리

    while front < len(queue):
        now = queue[front]
        front += 1

        if now == G:
            break

        for i in near[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)
    
    result = visited[G] if visited[G] != -1 else 0
    print(f"#{t} {result}")