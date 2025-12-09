T = int(input())

def partition(arr, start, end):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[start]
    left, right = start + 1, end

    while left <= right:
        while left <= right and arr[left] <= pivot:
            left += 1

        while left <= right and arr[right] >= pivot:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        
    arr[start], arr[right] = arr[right], arr[start]

    return right

def quick_sort(arr, left, right):
    if left < right:
        now = partition(arr, left, right)
        quick_sort(arr, left, now - 1)
        quick_sort(arr, now + 1, right)


for t in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    quick_sort(A, 0, N - 1)

    print(f'#{t} {A[N//2]}')