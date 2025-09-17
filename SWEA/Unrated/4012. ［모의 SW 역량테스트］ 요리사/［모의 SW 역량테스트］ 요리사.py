
from collections import deque

def synergy(my_list):
    total = 0
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            #이렇게 꺼내면 중복 없이 꺼내진다.
            ing1 = my_list[i]
            ing2 = my_list[j]
            total += ingredient[ing1][ing2] + ingredient[ing2][ing1]
    return total

def combination(indx,chosen): #인덱스로 해서 절반을 골랐으면 끝내기
    global min_diff

    if len(chosen) == (N // 2):
        other = [i for i in range(N) if i not in chosen]
        A = synergy(chosen)
        B = synergy(other)
        result = abs(A-B)
        min_diff = min(min_diff, result)

        return

    #계속 더하기만 하면 인덱스 에러
    if indx >= N:
        return
    #포함 하냐 안하냐 재귀돌리기!!
    combination(indx+1,chosen + [indx])
    combination(indx+1,chosen)


T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 음식의재료 수 = 행렬의 크기
    ingredient = [list(map(int,input().split())) for _ in range(N)]
    min_diff = float('inf')
    combination(0,[])
    print(f'#{tc} {min_diff}')
    


