T = int(input())

for i in range(1, T + 1) :
    K, N, M = map(int, input().split())
    charge_stations = list(map(int, input().split()))
    charge_stations.append(N) # 우리가 멈출 수 있는 곳
    
    now = 0 # 아직은 출발 전
    charge = 0 # 충전 횟수

    while now + K < N :  #충전 필요 없이 바로 갈 수 있는 경우 제외
        need_to_stop = 0  #멈춰야하는 충전소
    
        for station in reversed(charge_stations) : # 현재 주행가능한 최대를 찾기 위해서
            if now < station <= now + K :
                need_to_stop = station    # 최대한 가서 충전
                break               # 그 전의 충전소는 탐색필요 X
        if need_to_stop == 0 : # now 기준에서 충전소가 없었을 때
           charge = 0     # 혹시 중간까지는 충전해서 갈 수 있었더라도
           break          # 마지막까지 못간다면 0을 출력해야하므로
           

        now = need_to_stop  # 충전소 멈춘 기점으로 now에 할당
        charge += 1         # 멈출 때 마다 충전회수 +1
    
    print(f'#{i} {charge}')