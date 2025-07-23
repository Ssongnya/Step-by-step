T = int(input())

# for i in range(1, T + 1) :
#     N = int(input())
#     a_i = input()   # 인덱싱을 위해 문자열로
#     many = {}
#     for num in a_i :
#         if num not in many.keys() :
#             many[num] = 1
#         else :
#             many[num] += 1
    
#     print(f'#{i} {max(many)} {many[max(many)]}')
# ----> 오류발생 문자열로해서 생긴 오류인듯

for i in range(1, T + 1) :
    N = int(input())
    a_i = input()

    if len(a_i) != N :
        break   # 인덱싱을 위해 문자열로
    
    many = {}

    for num in a_i :
        if num in many.keys() :
            many[num] += 1
        else :
            many[num] = 1

    max_key, max_count = max(many.items(), key = lambda x : (x[1], int(x[0])))

    print(f'#{i} {max_key} {max_count}')