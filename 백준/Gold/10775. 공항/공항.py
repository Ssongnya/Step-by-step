import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x,  y):
    a = find(x)
    b = find(y)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


G = int(input())
P = int(input())

parent = [x for x in range(G + 1)]
count = 0

for _ in range(P):
    p = int(input())
    plane_p = find(p)

    if find(p) == 0:
        break
    
    union(plane_p, plane_p-1)

    count += 1

print(count)