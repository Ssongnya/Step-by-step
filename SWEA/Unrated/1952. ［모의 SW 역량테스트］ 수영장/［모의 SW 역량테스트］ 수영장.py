T = int(input())

for t in range(1, T + 1):
    day, month, three_month, year = map(int, input().split())

    plan = [0] + list(map(int, input().split()))
    months = [0] * 13        

    for i in range(1, 13):
        months[i] = min(months[i-1]  + plan[i]*day , months[i - 1]+ month )
        if i >= 3:
            months[i] = min(months[i], months[i-3] + three_month)
        
    result = min(months[12], year)
    print(f"#{t} {result}")