def subset(idx, chosen):
    global min_diff

    if idx >= N + 1:
        if isvalid(chosen):
            other = [x for x in range(1, N + 1) if x not in chosen]
            if isvalid(other):
                p1 = cal_pop(chosen)
                p2 = cal_pop(other)
                diff = abs(p1 - p2)
                min_diff = min(min_diff, diff)
        return

    subset(idx + 1, chosen + [idx])
    subset(idx + 1, chosen)


def cal_pop(lst):
    return sum(population[i] for i in lst)


def isvalid(lst):

    if not lst:
        return False
    
    used = [False for _ in range(N + 1)]
    stack = [lst[0]]
    used[lst[0]] = True

    while stack:
        now = stack.pop()
        for x in direct[now]:
            if not used[x] and x in lst:
                used[x] = True
                stack.append(x)
    
    return all([used[i] for i in lst])


N = int(input())

population = [0] + list(map(int, input().split()))
total_pop = sum(population)
direct = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    lst = list(map(int, input().split()))
    end = lst[1:]
    direct[i].extend(end)

min_diff = float('inf')
subset(1, [])

print(min_diff if min_diff != float('inf') else -1)