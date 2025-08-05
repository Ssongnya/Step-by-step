def find_max(lst):
    max_box = lst[0]
    max_idx = 0
    for idx in range(100):
        if lst[idx] > max_box :
            max_box = lst[idx]
            max_idx = idx
    return [max_box, max_idx]


def find_min(lst):
    min_box = lst[0]
    min_idx = 0
    for idx in range(100):
        if lst[idx] < min_box:
            min_box = lst[idx]
            min_idx = idx
    return [min_box, min_idx]

def flatten(lst):
    lst[find_max(lst)[1]] -= 1
    lst[find_min(lst)[1]] += 1
    return lst


for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump):
        flatten(boxes)

    print(f"#{t} {find_max(boxes)[0]- find_min(boxes)[0]}")