T = int(input())

for t in range(1, T+1) :
    str1 = input()
    str2 = input()

    count = {}

    for txt in str1:
        count[txt] = str2.count(txt)
    
        max_count = max(count.values())
    
    print(f'#{t} {max_count}')
