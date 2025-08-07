def find_sum(x, now_sum):
    global min_sum

    if now_sum >= min_sum:
        return
    
    if x == N :
        min_sum = now_sum
        return
    
    for y in range(N):
        if not visited[y]:
            visited[y] = True
            find_sum(x + 1, now_sum + nums[x][y])
            visited[y] = False



T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N

    min_sum = 10**10 + 1
    
    find_sum(0, 0)

    print(f"#{t} {min_sum}")