N = int(input())

col = [False] * N
cross1 = [False] * (2*N - 1)
cross2 = [False] * (2*N - 1)

count = 0

def nqueen(row):
    global count

    if row >= N:
        count += 1
        return
    
    for i in range(N):
        if not col[i] and not cross1[row + i] and not cross2[row - i + (N -1)]: 
            col[i], cross1[row + i], cross2[row - i + (N-1)] = True, True, True
            nqueen(row + 1)
            col[i], cross1[row + i], cross2[row - i + (N-1)] = False, False, False
    
nqueen(0)
print(count)