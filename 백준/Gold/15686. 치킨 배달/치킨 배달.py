def find_house(arr):
    global house_lst
    global chicken

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                house_lst.append((i, j))
            elif arr[i][j] == 2:
                chicken.append((i, j))

def chick_dist(lst):
    total = 0
    for hx, hy in house_lst:
        min_dist = float('inf')
        for cx, cy in lst:
            dist = abs(cx - hx) + abs(cy - hy)
            min_dist = min(dist, min_dist)
        total += min_dist
    return total

def m_store(idx, cnt, chosen):
    global chick_city_dist

    if cnt > M:
        return

    if idx >= len(chicken):
        if cnt == M:
            chick_city_dist = min(chick_dist(chosen), chick_city_dist)
        return
    
    x, y = chicken[idx][0], chicken[idx][1]

    m_store(idx + 1, cnt + 1, chosen + [(x, y)])
    m_store(idx + 1, cnt, chosen)


N, M = map(int, input().split())

city_map = [list(map(int, input().split())) for _ in range(N)]

house_lst = []
chicken = []

find_house(city_map)

chick_city_dist = float('inf')

m_store(0, 0, [])

print(chick_city_dist)