def move(idx, cnt, battery):
    global min_cnt

    if cnt >= min_cnt:
        return
    
    if idx >= N:
        min_cnt = min(min_cnt, cnt)
        return
    
    for i in range(1, battery[idx] + 1):
        move(idx + i, cnt + 1, battery)

T = int(input())

for t in range(1, T + 1):

    lst = list(map(int, input().split()))

    min_cnt = float('inf')

    N = lst[0]
    battery = [0] + lst[1:]

    move(1, -1, battery)

    print(f"#{t} {min_cnt}")
