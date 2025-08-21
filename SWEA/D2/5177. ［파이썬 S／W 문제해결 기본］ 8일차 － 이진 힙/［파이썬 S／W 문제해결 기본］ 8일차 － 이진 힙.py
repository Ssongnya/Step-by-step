def heap_append(lst, num):
    lst.append(num)

    i = len(lst) - 1  # 현재 노드 번호

    while i > 1:
        parent = i // 2
        if lst[parent] > lst[i]:
            lst[parent], lst[i] = lst[i], lst[parent]
            i = parent
        else:
            break

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    heap = [0]

    for num in nums:
        heap_append(heap, num)

    result = 0
    node = N

    while node > 1:
        node //= 2
        result += heap[node]

    print(f"#{t} {result}")