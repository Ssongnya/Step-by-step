for t in range(1, 11):
    N = int(input())
    
    board = [list(input().strip()) for _ in range(8)]

    
    count = 0

    for i in range(8):
        for j in range(8-N+1):
            reverse = True
            for n in range(N//2):
                if board[i][j + n] == board[i][N + j - 1 - n]:
                    continue
                else :
                    reverse = False
                    break
            if reverse :
                count += 1

    for j in range(8):
        for i in range(8-N+1):
            reverse = True
            for n in range(N//2):
                if board[i + n][j] == board[N + i - 1 - n][j]:
                    continue
                else :
                    reverse = False
                    break
            if reverse :
                count += 1

    print(f"#{t} {count}")