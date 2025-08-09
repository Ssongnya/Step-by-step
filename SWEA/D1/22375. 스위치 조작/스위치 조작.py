T = int(input())

def switch_on(bef, i):
    for j in range(i, len(bef)):
        bef[j] ^= 1
    return bef

def find_diff(bef, aft, i):
    for j in range(i, len(bef)):
        if bef[j] != aft[j]:
            return j
    return None

for t in range(1, T + 1):
    N = int(input())

    before = list(map(int, input().split()))
    after = list(map(int, input().split()))
    
    idx = find_diff(before, after, 0)
    count = 0
    
    while before != after and idx != None:
        count += 1
        before = switch_on(before, idx)
        idx = find_diff(before, after, idx)

    
    
    print(f"#{t} {count}")