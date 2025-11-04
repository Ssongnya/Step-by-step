N, K = map(int, input().split())
# N : 전체학생 수
# K : 한 방 최대 인원 수

girls = [0] * 7
boys = [0] * 7

rooms = 0

for _ in range(N):
    S, Y = map(int, input().split())
    # S : 성별 (0-여, 1-남)
    # Y : 학년
    if S == 0:
        if girls[Y] == 0:
            rooms += 1
            girls[Y] = 1
        elif girls[Y] < K:
            girls[Y] += 1
            if girls[Y] == K:
                girls[Y] = 0
    else:
        if boys[Y] == 0:
            rooms += 1
            boys[Y] = 1
        elif boys[Y] < K:
            boys[Y] += 1
            if boys[Y] == K:
                boys[Y] = 0

print(rooms)
