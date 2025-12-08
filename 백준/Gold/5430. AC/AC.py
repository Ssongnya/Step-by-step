from collections import deque

def Rfunction(reverse_sign):
    return not reverse_sign

def Dfunction(arr, reverse_sign):
    if not arr:
        return False
    if reverse_sign:
        arr.pop()
    else:
        arr.popleft()
    return arr


T = int(input())

for _ in range(T):
    fun_lst = input().strip()
    n = int(input())
    arr_str = input().strip()

    if n == 0:
        num_lst = deque()
    else:
        num_lst = deque(arr_str[1:-1].split(','))

    reverse_sign = False
    error = False

    for f in fun_lst:
        if f == 'R':
            reverse_sign = Rfunction(reverse_sign)

        else:
            num_lst = Dfunction(num_lst, reverse_sign)
            if num_lst is False:
                print("error")
                error = True
                break

    if error:
        continue

    if reverse_sign:
        num_lst.reverse()

    print("[" + ",".join(num_lst) + "]")
