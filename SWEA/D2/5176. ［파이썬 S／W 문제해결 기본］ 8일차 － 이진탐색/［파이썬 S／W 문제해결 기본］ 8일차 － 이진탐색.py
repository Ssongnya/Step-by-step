T = int(input())

def inorder(now, n, nodes, num):
    
    if now <= n:
        num = inorder(now * 2, n, nodes, num)
        nodes[now] = num
        num += 1

        num = inorder(now * 2 + 1, n, nodes, num) 


    return num

for t in range(1, T + 1):
    N = int(input())

    nodes = [0] * (N + 1)

    inorder(1, N, nodes, 1)

    print(f"#{t} {nodes[1]} {nodes[N//2]}")