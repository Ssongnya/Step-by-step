k = int(input())
signs = input().split()

visited = [False] * 10

max_num = ""
min_num = "9" * (k + 1)

def isvalid(sign, x, y):
    if sign == '<':
        return x < y
    else:
        return x > y

def find(idx, num):

    global min_num, max_num

    if idx >= k + 1:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return
    
    for i in range(10):
        if not visited[i]:
            if idx == 0:
                visited[i] = True
                find(idx + 1, num + str(i))
                visited[i] = False
            else:
                if isvalid(signs[idx-1], int(num[-1]), i):
                    visited[i] = True
                    find(idx + 1, num + str(i))
                    visited[i] = False

find(0, "")

print(max_num)
print(min_num)