T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    words_board = [list(input().strip()) for _ in range(N)]

    found = False

    for i in range(N):
        for j in range(N - M + 1):
            find_word = words_board[i][j:j+M]
            if find_word == find_word[::-1]:
                found = "".join(find_word)
                break
        if found:
            break

    if not found:
        for i in range(N - M + 1):
            for j in range(N):
                find_word = [words_board[i+k][j] for k in range(M)]
                if find_word == find_word[::-1]:
                    found = "".join(find_word)
                    break
            if found:
                break

    print(f"#{t} {found}")