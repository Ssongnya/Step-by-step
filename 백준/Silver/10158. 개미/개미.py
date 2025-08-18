def reflect(start, time, limit):
    now = (start + time) % (2 * limit)
    return limit - abs(limit - now)

width, height = map(int, input().split())
start_x, start_y = map(int, input().split())
time = int(input())

x = reflect(start_x, time, width)
y = reflect(start_y, time, height)

print(x, y)
