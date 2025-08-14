N = int(input())
switches = list(map(int, input().split()))
students = int(input())

def boy(lst, num):
    n = len(lst)
    for i in range(n):
        if (i+1) % num == 0:
            lst[i] ^= 1

    return lst

def girl(lst, num):
    n = len(lst)
    idx = num - 1
    left = idx - 1
    right = idx + 1
    
    while left >= 0 and right < n and lst[left] == lst[right]:
        left -= 1
        right += 1

    for i in range(left + 1, right):
        lst[i] ^= 1
    return lst

for i in range(students):
    sex, num = map(int, input().split())
    if sex == 1:
        boy(switches, num)
    else:
        girl(switches, num)

for j in range(0, N, 20):
    print(*switches[j:j+20])
