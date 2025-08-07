
def find_end(arr):
    n = len(arr)
    for col in range(n):
         if arr[99][col] == 2:
             return col


def bottom_to_top(x, y):

    while x > 0:
        visited[x][y] = True

        yes_or_no = False
        for i, j in have_to_move:
            mx, my = x + i, y + j
            if 0 <= my < 100 and ladder[mx][my] == 1 and not visited[x][my]:
                y = my
                yes_or_no = True

        if not yes_or_no:
            x -= 1

    return y


for _ in range(10):
    T = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]
    visited = [[False]*100 for _ in range(100)]
    have_to_move = [(0, 1), (0, -1)]

    bottom_col = find_end(ladder)
    top_col = bottom_to_top(99, bottom_col)

    print(f"#{T} {top_col}")
