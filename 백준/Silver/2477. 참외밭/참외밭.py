N = int(input())

directions = []
height = []
length = []

for _ in range(6):
    direct, long = map(int, input().split())
    directions.append([direct,long])
    if direct == 3 or direct == 4:
        height.append(long)
    else:
        length.append(long)

small_w, small_h = 0, 0

find_width = 1
for i in range(6):
    if directions[i][0] == directions[(i + 2)%6][0]:
        find_width *= directions[(i+1)%6][1]


max_height = max(height)
max_length = max(length)

total_width = max_height * max_length - find_width

print(total_width*N)