def find_min_sum(idx, hap):
    global min_hap

    if hap >= min_hap:
        return

    if len(visited) == N:
        total = hap + arr[idx][0]
        min_hap = min(min_hap, total)
        return
    
    for i in range(1, N):
        if i not in visited:
            visited.add(i)
            find_min_sum(i, hap + arr[idx][i])
            visited.remove(i)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = set([0])
    min_hap = float('inf')

    find_min_sum(0, 0)
    print(f"#{t} {min_hap}")

