def front_check(lst, num):
    n = len(lst)
    for i in range(num, n):
        if lst[i] > lst[num]:
            return True
    return False

N = int(input())

graph = [tuple(map(int, input().split())) for _ in range(N)]

end_idx = max(x for x, _ in graph)

graph_lst = [0] * (end_idx + 1)

for x, y in graph:
    graph_lst[x] = y

max_h = max(graph_lst)

first_max = -1

for hx, hy in enumerate(graph_lst):
    if hy == max_h:
        first_max = hx
        break

last_max = -1

for hx, hy in enumerate(graph_lst):
    if hy == max_h:
        last_max = hx

width = 0

left_max = 0
for i in range(first_max):
    if graph_lst[i] > left_max :
        left_max = graph_lst[i]
    width += left_max


right_max = 0

for j in range(end_idx, last_max, -1):
    if graph_lst[j] > right_max:
        right_max = graph_lst[j]
    width += right_max

middle = max_h * (last_max - first_max + 1)

print(width + middle)