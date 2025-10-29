def solution(users, emoticons):
    answer = []
    discount = [10, 20, 30, 40]
    percent = [0.9, 0.8, 0.7, 0.6]
    
    n = len(users)
    e = len(emoticons)
    
    cost = [0] * e # 각 이모티콘 할인률(인덱스)
    
    max_plus = 0
    max_cost = 0
    
    def dfs(idx):
        
        nonlocal max_plus, max_cost
        
        if idx == e:
            
            plus_cnt = 0
            total_cost = 0
            
            for p in range(n):
                cost_hap = 0
                for c in range(e):
                    if users[p][0] <= discount[cost[c]]:
                        cost_hap += emoticons[c] * percent[(cost[c])]
                if cost_hap >= users[p][1]:
                    plus_cnt += 1
                else:
                    total_cost += cost_hap
            
            if plus_cnt > max_plus or (plus_cnt == max_plus and total_cost > max_cost):
                max_plus = plus_cnt
                max_cost = total_cost
            return
        
        for i in range(4):
            cost[idx] = i
            dfs(idx + 1)
            
    dfs(0)
    answer.append(max_plus)
    answer.append(max_cost)
    return answer