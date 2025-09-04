def switch(lst, count):
    global max_hap

    if count == n:
        max_hap = max(max_hap, int("".join(lst)))
        return
    
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            lst[i], lst[j] = lst[j], lst[i]
            now = ("".join(lst), count)
            if now not in visited:
                visited.add(now)
                switch(lst, count + 1)
            lst[i], lst[j] = lst[j], lst[i]


T = int(input())

for t in range(1, T + 1):
    num, N = input().split()

    n = int(N)

    nums = list(num)

    visited = set()
    max_hap = 0

    switch(nums, 0)

    print(f"#{t} {max_hap}")

