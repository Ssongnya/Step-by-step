T = int(input())

def dfs(row, current_sum):
    global min_sum

    # 가지치기: 현재 합이 이미 최소 합보다 크면 중단
    if current_sum >= min_sum:
        return

    # 모든 행을 다 선택했으면 최소 합 갱신
    if row == n:
        min_sum = current_sum
        return

    # 현재 행에서 가능한 열 선택
    for col in range(n):
        if not used[col]:  # 아직 사용 안한 열이면 선택 가능
            used[col] = True
            dfs(row + 1, current_sum + cost[row][col])
            used[col] = False  # 원상복구 (백트래킹)

for tc in range(1, T + 1):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]

    used = [False] * n  # 각 열 선택 여부
    min_sum = float('inf')

    dfs(0, 0)
    print(f"#{tc} {min_sum}")
