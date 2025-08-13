for _ in range(1, 11):
    T, N = map(int, input().split())
    A, B = 0, 99

    nums = list(map(int, input().split()))
    size = [[] for _ in range(100)]

    for i in range(0, 2*N, 2):
        size[nums[i]].append(nums[i+1])

    visited = [False] * 100
    found = False
    stack = [0]
    visited[0] = True

    while len(stack) > 0:
        now = stack.pop()

        if now == 99:
            found = True
            break

        for j in size[now]:
            if not visited[j]:
                stack.append(j)
                visited[j] = True

    result = 1 if found else 0
    print(f"#{T} {result}")