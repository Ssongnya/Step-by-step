N = int(input())

eggs = [list(map(int, input().split())) for _ in range(N)]


max_broken = -1

def egg_break(now):
    """
    손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다. 
    단, 손에 든 계란이 깨졌거나 
    깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다.
    """
    global max_broken

    if now >= N:
        broken_cnt = 0
        for d, _ in eggs:
            if d <= 0:
                broken_cnt += 1
        max_broken = max(max_broken, broken_cnt)
        return

    # 손에 든 계란이 깨졌거나
    if eggs[now][0] <= 0:
        egg_break(now+1)
        return
    
    # 깨지지 않은 다른 계란이 없으면
    can_hit = False
    for i in range(N):
        if i == now or eggs[i][0] <= 0:
            continue

        can_hit = True

        # 계란으로 계란을 치게 되면 각 계란의 내구도는 상대 계란의 무게만큼 깎이게 된다
        eggs[now][0] -= eggs[i][1]
        eggs[i][0] -= eggs[now][1]

        # 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행한다. 
        egg_break(now + 1)

        # 백트래킹
        eggs[now][0] += eggs[i][1]
        eggs[i][0] += eggs[now][1]
    
    # 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다
    if not can_hit:
        egg_break(now + 1)

egg_break(0) # 0번째(처음) 계란부터 깨기 시작
print(max_broken)