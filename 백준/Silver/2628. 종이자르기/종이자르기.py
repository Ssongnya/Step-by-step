col, row = map(int, input().split())

N = int(input())
col_cut = []
row_cut = []

for _ in range(N):
    col_or_row, num = map(int, input().split())
    if col_or_row == 0:
        row_cut.append(num)
    else :
        col_cut.append(num)

col_cut.extend([0, col])
row_cut.extend([0, row])

col_cut.sort()
row_cut.sort()

max_w = 0

for i in range(1, len(col_cut)):
    max_w = max(max_w, col_cut[i] - col_cut[i-1])

max_h = 0

for j in range(1, len(row_cut)):
    max_h = max(max_h, row_cut[j] - row_cut[j-1])

print(max_h * max_w)
