T = int(input())
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# 부분집합 함수 만들어 보기

def subset(num, count, hap) : #부분집합에 넣을 숫자, 갯수, 합

    global total

    if count > N or hap > K :
        return 0
    
    if num > 12 :   # 1부터 12까지 선택되는지 안되는지 다 확인한 후에,
        if count == N and hap == K :    # 갯수와 합이 N, K와 동일하면
            total += 1     # 부분집합 갯수 +1
        return
    
    subset(num + 1, count + 1, hap + num)     # num 을 선택해서 count를 1 올려준다.

    subset(num + 1, count, hap)   # num을 선택하지 않으면 count, hap 패스



for t in range(1, T + 1) :
    N, K = map(int, input().split())

    total = 0   # 초기화 되면 안되고 누적 되어야 함

    subset(1, 0, 0) # 1부터 포함되는지 안되는지 확인
    print(f"#{t} {total}")