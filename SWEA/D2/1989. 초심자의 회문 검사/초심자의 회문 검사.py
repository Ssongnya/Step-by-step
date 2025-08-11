T = int(input())

for t in range(1, T + 1):
    word = input()
    N = len(word)
    
    reverse = True


    for i in range(N//2+1):
        if word[i] == word[N - 1 - i]:
            continue
        else:
            reverse = False
            print(f"#{t}", 0)
            break

    if reverse :
        print(f"#{t}", 1)