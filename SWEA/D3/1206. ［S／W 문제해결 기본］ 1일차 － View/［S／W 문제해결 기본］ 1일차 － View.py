for t in range(1, 11):
    N = int(input())

    buildings = list(map(int, input().split()))
    sunlight = 0

    for b in range(2, N-2):
        max_diff = 0
        brange = [buildings[b-2], buildings[b-1], buildings[b+1], buildings[b+2]]
        if buildings[b] > max(brange):
            sunlight += buildings[b] - max(brange)

    print(f"#{t} {sunlight}")


