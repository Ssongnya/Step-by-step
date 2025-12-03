must = ['a', 'n', 't', 'i', 'c']

N, K = map(int, input().split())
words = [input().strip() for _ in range(N)]

if K < 5:
    print(0)
    exit()

if K == 26:
    print(N)
    exit()

find = []

for word in words:
    s = set()
    for w in word[4:-4]:
        if w not in must:
            s.add(w)    
    find.append(s)

visited = [False] * 26
for m in must:
    visited[ord(m) - 97] = True

result = 0

def choose(idx, cnt):
    global result

    if cnt == (K - 5):
        possible = 0
        for s in find:
            isvalid = True
            for alpha in s:
                if not visited[ord(alpha) - 97]:
                    isvalid = False
                    break
            if isvalid:
                possible += 1
        if possible > result:
            result = possible
        return
    if idx >= 26:
        return
    
    if visited[idx]:
        choose(idx + 1, cnt)
    else:
        visited[idx] = True
        choose(idx + 1, cnt + 1)

        visited[idx] = False
        choose(idx + 1, cnt)

choose(0, 0)
print(result)
