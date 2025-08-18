T = int(input())

for tc in range(1, T + 1):
    t = int(input())
    scores = list(map(int, input().split()))

    max_count = -1
    max_lst = []
    for s in scores:
        count = scores.count(s)
        if count > max_count:
            max_count = count
    
    for s in scores:
        if scores.count(s) == max_count:
            max_lst.append(s)

    print(f"#{t}", max(max_lst))

