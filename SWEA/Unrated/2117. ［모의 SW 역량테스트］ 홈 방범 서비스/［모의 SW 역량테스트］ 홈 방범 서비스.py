def k_range(k, ox, oy, x, y):
    if abs(ox - x) + abs(oy -y) < k:
        return True
    return False



T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    max_count = -1
    
    for i in range(N):
        for j in range(N):
            for k in range(1, N+2):
                cost = k*k + (k-1)*(k-1)
                house = 0
                
                for x in range(N):
                    for y in range(N):
                        if my_map[x][y] == 1 and k_range(k, i, j, x, y):
                            house += 1
                
                if house*M >= cost and house >= max_count:
                    max_count = house

    print(f"#{t} {max_count}")
