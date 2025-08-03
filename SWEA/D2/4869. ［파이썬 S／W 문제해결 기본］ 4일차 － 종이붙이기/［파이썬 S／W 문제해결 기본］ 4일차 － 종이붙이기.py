# 재귀함수
def paper_connect(N) :
    paper = [1, 3]
    if (N/10) > 2 :
        return 2*paper_connect(N-20) + paper_connect(N-10)
    elif N/10 == 2 :
        return paper[1]
    else :
        return paper[0]


T = int(input())

for t in range(1, T+1) :
    N = int(input())
    print(f'#{t} {paper_connect(N)}')