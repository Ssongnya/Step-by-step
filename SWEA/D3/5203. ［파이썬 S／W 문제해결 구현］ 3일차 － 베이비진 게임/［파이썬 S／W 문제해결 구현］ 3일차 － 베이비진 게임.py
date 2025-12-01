T = int(input())

def my_run(arr):
    if len(arr) < 3:
        return False
    for i in range(8):
        if arr[i] and arr[i+1] and arr[i+2]:
            return True
    return False

def triplet(arr):
    if len(arr) < 3:
        return False
    for i in range(10):
        if arr[i] >= 3:
            return True
    return False

for t in range(1, T + 1):
    
    whole = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    find = False
    for i in range(12):
        if i % 2 == 0:
            n = whole[i]
            p1[n] += 1
        else:
            n = whole[i]
            p2[n] += 1

        if my_run(p1) or triplet(p1):
            print(f"#{t} {1}")
            find = True
            break

        elif my_run(p2) or triplet(p2):
            print(f"#{t} {2}")
            find = True
            break
    if not find:
        print(f"#{t} {0}")