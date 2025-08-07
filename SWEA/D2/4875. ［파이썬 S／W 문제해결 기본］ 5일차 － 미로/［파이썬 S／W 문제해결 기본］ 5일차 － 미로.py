def start(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2 :
                start = (i, j)
    return start


def end(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3 :
                end = (i, j)
    return end

def find_0 (x, y):

    if (x, y) == end_place:
        return True
    
    else :
        
        visited[x][y] = True
        for i, j in near:
            nx = x + i
            ny = y + j

            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and not visited[nx][ny]:
                if find_0(nx, ny):
                    return True
            
        visited[x][y] = False
        return False

T = int(input())

for t in range(1, T + 1):

    N = int(input())

    maze = [list(map(int, input().strip())) for _ in range(N)]

    visited = [[False]*N for _ in range(N)]

    near = [(1, 0), (-1, 0), (0, -1), (0, 1)]


    start_place = start(maze)
    end_place = end(maze)

                
    if find_0(*start_place) :
        print(f"#{t} 1")
    else :
        print(f"#{t} 0")