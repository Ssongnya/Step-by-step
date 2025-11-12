N, M = map(int, input().split())

board = [input().strip() for _ in range(N)]

min_count = 64


for i in range(N-7):
    for j in range(M-7):
        
        paint_w = 0
        paint_b = 0

        for x in range(8):
            for y in range(8):
                now = board[i+x][j+y]
                if (x+y) % 2 == 0:
                    if now != 'W':
                        paint_w += 1
                    if now != 'B':
                        paint_b += 1
                else:
                    if now != 'B':
                        paint_w += 1
                    if now != 'W':
                        paint_b += 1

        min_count = min(min_count, paint_b, paint_w)

print(min_count)
                