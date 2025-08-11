T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())

    near = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        near[a].append(b)
        near[b].append(a)   # 양방향에 전부 간선 정보 입력
    
    S, G = map(int, input().split())

    visited = [-1] * (V + 1)    # -1로 초기화 0번 인덱스는 안쓸거니까 V+1
    queue = [S]
    front = 0
    visited[S] = 0

    while front < len(queue):
        now = queue[front]
        front += 1

        if now == G:
            break
    
        for j in near[now]:
            if visited[j] == -1 :
                visited[j] = visited[now] + 1
                queue.append(j)

    result = visited[G] if visited[G] != -1 else 0
    print(f"#{t} {result}")