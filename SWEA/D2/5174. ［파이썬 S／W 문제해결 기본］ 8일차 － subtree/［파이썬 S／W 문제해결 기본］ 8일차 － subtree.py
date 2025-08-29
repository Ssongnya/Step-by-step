class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

def subtree(node):
    global count

    for child in node.children:
        count += 1
        subtree(child)


T = int(input())

for t in range(1, T + 1):
    E, N = map(int, input().split())
    direct = list(map(int, input().split()))

    nodes = {}

    for i in range(0, len(direct), 2):
        p, c = direct[i], direct[i + 1]   

        if p not in nodes:
            nodes[p] = Node(p)
        if c not in nodes:
            nodes[c] = Node(c)
        
        nodes[p].add_child(nodes[c])

    count = 1
    subtree(nodes[N])
    
    print(f"#{t} {count}")
