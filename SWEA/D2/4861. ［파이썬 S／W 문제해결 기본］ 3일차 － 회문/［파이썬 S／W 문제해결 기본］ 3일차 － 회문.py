T = int(input())

for t in range(1, T + 1) :
    N, M = map(int, input().split())
    result = []

    # 배열 입력 받기
    grid = []
    for num in range(N):
        grid.append(list(input().strip())) # 리스트로 저장
    
    # 가로 검색
    for row in range(N):
        for column in range(N - M + 1) :
            find_row = grid[row][column:column + M]
            if find_row == find_row[::-1] :
                result.append("".join(find_row)) # 문자열 반환
    
    # 세로 검색

    for column in range(N): # 열 고정 후 같은 열 끼리 비교
        for row in range(N - M + 1) : # 시작 행
            col_txt = []
            for find_col in range(M) : # M 길이만큼 문자 추출
                col_txt.append(grid[row + find_col][column])
            if col_txt == col_txt[::-1] :
                result.append("".join(col_txt))
    
    print(f'#{t} {result[0]}')