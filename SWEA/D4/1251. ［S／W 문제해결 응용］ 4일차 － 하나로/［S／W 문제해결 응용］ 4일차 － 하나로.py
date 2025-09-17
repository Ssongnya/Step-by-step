
T = int(input())

for t in range(1, T + 1):

    N = int(input())

    x_coor = list(map(int, input().split()))
    y_coor = list(map(int, input().split()))

    xy_coor = list(zip(x_coor, y_coor))

    E = float(input())

    visited = [False] * N
    cost = [float('inf')] * N
    cost[0] = 0

    total_cost = 0

    for _ in range(N):
        u = -1
        min_val = float('inf')

        for i in range(N):
            if not visited[i] and cost[i] < min_val:
                min_val = cost[i]
                u = i
        
        visited[u] = True
        total_cost += min_val

        for j in range(N):
            if not visited[j]:
                dx = xy_coor[j][0] - xy_coor[u][0]
                dy = xy_coor[j][1] - xy_coor[u][1]

                dist2 = dx*dx + dy*dy

                if dist2 < cost[j]:
                    cost[j] = dist2

    result = round(total_cost * E)
    print(f"#{t} {result}")