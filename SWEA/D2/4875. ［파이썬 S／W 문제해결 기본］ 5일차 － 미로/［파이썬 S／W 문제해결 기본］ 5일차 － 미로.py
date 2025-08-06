T = int(input())

for t in range(1, T + 1):
    N = int(input())

    maze = [[int(x) for x in input().strip()] for _ in range(N)]

    visited = [[0]*N for _ in range(N)]
    near = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def is_Valid(x, y):
        return 0 <= x < N and 0 <= y < N and maze[x][y] != 1 and not visited[x][y]
    
    def start(arr):
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 2:
                    return (i, j)
    

    def end(arr):
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 3:
                    return (i, j)
        
    def backtrack(x, y):
        if (x, y) == end(maze):
            return True
        
        visited[x][y] = 1
        for dx, dy in near:
            nx, ny = x + dx, y + dy
            if is_Valid(nx, ny):
                if backtrack(nx, ny):
                    return True
        visited[x][y] = 0
        return 0
    
    start_place = start(maze)

    if backtrack(*start_place):
        print(f"#{t}", 1)
    else:
        print(f"#{t}", 0)

