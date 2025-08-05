T = int(input())

for t in range(1, T+1):

    N = int(input())

    bus_stop = [0] * 5000

    for i in range(N):
        A, B = map(int, input().split())
        for k in range(A-1, B):
            bus_stop[k] += 1


    P = int(input())
    c_lst = [int(input()) for _ in range(P)]

    print(f"#{t}", end=' ')
    result = [str(bus_stop[k-1]) for k in c_lst]
    print(" ".join(result))
