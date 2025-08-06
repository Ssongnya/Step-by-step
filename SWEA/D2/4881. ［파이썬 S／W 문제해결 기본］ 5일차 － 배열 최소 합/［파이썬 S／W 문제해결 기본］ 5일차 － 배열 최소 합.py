T = int(input())

def backtrack(row, current_sum):
    global min_sum
    # 가지치기: 현재 합이 이미 최소 합보다 크면 중단
    if current_sum >= min_sum:
        return

    # 모든 행에서 숫자를 선택한 경우
    if row == N:
        min_sum = current_sum
        return

    # 현재 행에서 각 열을 선택
    for col in range(N):
        if not visited[col]:  # 해당 열이 선택되지 않았으면
            visited[col] = True
            backtrack(row + 1, current_sum + grid[row][col])
            visited[col] = False  # 원상복구 (백트래킹)

for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N  # 열 방문 여부 체크
    min_sum = float('inf')  # 최소 합 초기화

    backtrack(0, 0)  # 0행부터 시작

    print(f"#{t} {min_sum}")
