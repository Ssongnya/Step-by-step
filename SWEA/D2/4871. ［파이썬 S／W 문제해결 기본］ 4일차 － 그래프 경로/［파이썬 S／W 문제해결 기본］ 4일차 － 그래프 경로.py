T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())

    direct = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        direct[a].append(b)

    S, G = map(int, input().split())

    stack = [S]
    visited = [False] * (V + 1)
    visited[S] = False
    found = False

    while len(stack) > 0:
        now = stack.pop()

        if now == G:
            found = True
            break

        for i in direct[now]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True

    result = 1 if found else 0

    print(f"#{t} {result}")