def merge_sort(arr):
    global count
    
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    if left[-1] > right[-1]:
        count += 1

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    count = 0
    sorted_arr = merge_sort(arr)

    print(f"#{t} {sorted_arr[N//2]} {count}")
