for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for d in range(dump):
        max_idx = boxes.index(max(boxes))
        min_idx = boxes.index(min(boxes))

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    print(f"#{t} {max(boxes)-min(boxes)}")