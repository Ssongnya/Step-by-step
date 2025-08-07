T = int(input())


def binary(page, wanted_page):

    left = 1
    right = page

    count = 0

    while left <= right:
        mid = (left + right) // 2
        count += 1

        if wanted_page == mid:
            return count
        elif wanted_page > mid:
            left = mid
        else:
            right = mid

    return count


for t in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    count_A = binary(P, Pa)
    count_B = binary(P, Pb)

    if count_A < count_B:
        result = "A"
    elif count_A == count_B:
        result = 0
    else:
        result = "B"

    print(f"#{t} {result}")
