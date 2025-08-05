for t in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    find = 0

    for i in range(2, len(building) - 2):
        left2 = building[i - 2]
        left1 = building[i - 1]
        right1 = building[i + 1]
        right2 = building[i + 2]

        if left2 > building[i] or left1 > building[i] or right2 > building[i] or right1 > building[i]:
            continue
        else:
            diff1 = building[i] - left2
            diff2 = building[i] - left1
            diff3 = building[i] - right2
            diff4 = building[i] - right1

            min_diff = diff1

            if diff2 < min_diff:
                min_diff = diff2
            if diff3 < min_diff:
                min_diff = diff3
            if diff4 < min_diff:
                min_diff = diff4

            find += min_diff

    print(f'#{t} {find}')
