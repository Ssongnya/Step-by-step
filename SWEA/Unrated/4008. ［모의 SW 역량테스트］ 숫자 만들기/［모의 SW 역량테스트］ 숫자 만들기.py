def calculate(idx, now, oper):
    global max_val, min_val

    if idx >= N:
        max_val = max(now, max_val)
        min_val = min(now, min_val)
        return
    
    nxt = int(nums[idx])

    for i in range(4):
        if oper[i] > 0 :
            curr_oper = oper[:]
            curr_oper[i] -= 1

            if i == 0 :
                calculate(idx + 1, now + nxt, curr_oper)
            elif i == 1 :
                calculate(idx + 1, now - nxt, curr_oper)
            elif i == 2 :
                calculate(idx + 1, now * nxt, curr_oper)
            elif i == 3 :
                if nxt != 0:
                    if now < 0:
                        calculate(idx + 1, -(-now // nxt), curr_oper)
                    else:
                        calculate(idx + 1, now // nxt, curr_oper)


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    oper_num = list(map(int, input().split()))
    nums = input().split()
    
    max_val = -100000001
    min_val = 100000001

    calculate(1, int(nums[0]), oper_num)

    print(f"#{t} {max_val - min_val}")