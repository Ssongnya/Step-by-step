T = int(input())


        

def dfs_stack(graph, start):
    visited = []
    stack = [start]

    # 스택이 빌 때까지 반복
    while stack:
        node = stack.pop()  # 스택의 가장 위(마지막) 노드를 꺼냄
        if node not in visited:  # 아직 방문하지 않았다면
            visited.append(node)  # 방문 리스트에 추가
            # 현재 노드와 연결된 인접 노드를 확인
            # reversed를 쓰는 이유: 스택은 LIFO라서 역순으로 넣어야 작은 번호부터 방문 가능
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)  # 방문하지 않은 노드를 스택에 추가
    return visited

for t in range(1, T+1) :
    V, E = map(int, input().split())
    direct = []
    for i in range(E):
        direct.append(list(map(int, input().split())))
    
    S, G = map(int, input().split())
    
    graph = {k : [] for k in range(1, V+1)}

    for e in direct :
        a, b = e
        graph[a].append(b)
    
    

    if G in dfs_stack(graph, S):
        print(f'#{t}', 1)
    else :
        print(f'#{t}', 0)