"""
우선순위 큐인듯?
치즈의 양에 따라 녹는 시간이 달라서 꺼내지는 순서가 달라짐
피자는 front에서만 넣거나 뺄 수 있음
M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 
화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 
이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
"""
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    cheese_lst = list(map(int, input().split()))

    oven = [] 
    for i in range(N):
        oven.append([i+1, cheese_lst[i]])  # 피자 번호 매기고, 치즈 양 넣기
    
    next_pizza = N

    while len(oven) > 1 :  # 마지막 한 개 남을 때까지
        pizza_num, cheese = oven.pop(0)
        cheese //= 2
        
        if cheese > 0 :
            oven.append([pizza_num, cheese])
        else :  # 치즈 다 녹으면
            if next_pizza < M : # 대기 피자 있으면 넣고
                oven.append([next_pizza + 1, cheese_lst[next_pizza]])
                next_pizza += 1 # 최종 인덱스는 1 더 더해주기

    print(f"#{t} {oven[0][0]}") # [0][0] -> 피자 번호

