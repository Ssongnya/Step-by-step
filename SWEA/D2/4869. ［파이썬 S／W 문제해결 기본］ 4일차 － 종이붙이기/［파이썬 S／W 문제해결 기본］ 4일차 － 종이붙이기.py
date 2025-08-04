# DP 사용
def paper_connect(N) :
    paper = [1, 3]
    for i in range(2, N//10):
        num = paper[i-1] + paper[i-2] * 2
        paper.append(num)
    n = len(paper) - 1
    return paper[n]


T = int(input())

for t in range(1, T+1) :
    N = int(input())
    print(f'#{t} {paper_connect(N)}')