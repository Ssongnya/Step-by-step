
def find_direct(graph, start):
    visited = []    
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for near in graph[node]:
                if near not in visited:
                    stack.append(near)
    return visited


T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())
    direct = {x: [] for x in range(1, V+1)}
    for _ in range(E):
        s, e = map(int, input().split())
        direct[s].append(e)

    S, G = map(int, input().split())

    if G in find_direct(direct, S):
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")
