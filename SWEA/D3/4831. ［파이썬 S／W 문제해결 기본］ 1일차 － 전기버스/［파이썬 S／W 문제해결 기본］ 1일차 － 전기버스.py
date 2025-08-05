T = int(input())

for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge_station = list(map(int, input().split()))
    charge_station.append(N)

    now = 0
    charge = 0

    while now + K < N :
        need_to_stop = 0

        for stop in reversed(charge_station):
            if now < stop <= now + K :
                need_to_stop = stop
                break
        now = need_to_stop
        charge += 1

        if need_to_stop == 0 :
            charge = 0
            break
    print(f"#{t} {charge}")