
def energy(now, n, curr_energy, visited): 
    global min_total

    if curr_energy >= min_total:
        return
    
    if len(visited) == n:
        total = curr_energy + e[now][0]
        min_total = min(min_total, total)
        return
    
    for i in range(1, n):
        if i not in visited:
            visited.add(i)
            energy(i, n, curr_energy + e[now][i], visited)
            visited.remove(i)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]

    visited = set([0])
    min_total = 10000000000

    energy(0, N, 0, visited)
    print(f"#{t} {min_total}")   