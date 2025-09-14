dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    answer = -1

    for i in range(N):
        for j in range(N):
            # 두 변의 길이 a, b 시도
            for a in range(1, N):
                for b in range(1, N):
                    x, y = i, j
                    desserts = {cafe[x][y]}
                    valid = True

                    for d, step in enumerate([a, b, a, b]):
                        dx, dy = dirs[d]
                        for _ in range(step):
                            x += dx
                            y += dy
                            # 범위 체크
                            if not (0 <= x < N and 0 <= y < N):
                                valid = False
                                break
                            # 마지막 좌표가 출발점일 경우는 중복 검사 X
                            if (x, y) != (i, j) and cafe[x][y] in desserts:
                                valid = False
                                break
                            desserts.add(cafe[x][y])
                        if not valid:
                            break

                    # 출발점으로 정확히 돌아왔는지 확인
                    if valid and (x, y) == (i, j):
                        # 최소한 a, b가 2 이상이어야 "사각형"을 그림
                        if a > 0 and b > 0:
                            answer = max(answer, len(desserts))

    print(f"#{t} {answer}")
