T = int(input())


def length(arr, x, y):
    
    if arr[x][y] != 'o':
        leng[x][y] = 0
        return False
    
    if y > 0 :
        leng[x][y] = leng[x][y-1] + 1
    else :
        leng[x][y] = 1

    if leng[x][y] >= 5 :
        return True
    
    return False
    

def height(arr, x, y):
    
    if arr[x][y] != 'o':
        high[x][y] = 0
        return False
    
    if x > 0 :
        high[x][y] = high[x-1][y] + 1
    else :
        high[x][y] = 1

    if high[x][y] >= 5 :
        return True

    return False


def maincross(arr, x, y):
    
    if arr[x][y] != 'o':
        mainc[x][y] = 0
        return False
    
    if x > 0 and y > 0 :
        mainc[x][y] = mainc[x-1][y-1] + 1
    else :
        mainc[x][y] = 1
    
    if mainc[x][y] >= 5 :
        return True

    return False



def subcross(arr, x, y):
    
    if arr[x][y] != 'o':
        subc[x][y] = 0
        return False
    
    if x > 0 and y + 1 < N:
        subc[x][y] = subc[x-1][y+1] + 1
    else :
        subc[x][y] = 1
    
    if subc[x][y] >= 5 :
        return True   

    return False



for t in range(1, T + 1):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]

    leng = [[0]*N for _ in range(N)]
    high = [[0]*N for _ in range(N)]
    mainc = [[0]*N for _ in range(N)]
    subc = [[0]*N for _ in range(N)]

    result = False

    for i in range(N):
        if result :
            break
        for j in range(N):
            case1 = length(grid, i, j)
            case2 = height(grid, i, j)
            case3 = maincross(grid, i, j)
            case4 = subcross(grid, i, j)

            if case1 or case2 or case3 or case4:
                print(f"#{t} YES")
                result = True
                break
    
    if not result :
        print(f"#{t} NO")