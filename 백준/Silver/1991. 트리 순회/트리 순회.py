import sys
alpha_dict = {chr(ord('A') + i): i for i in range(26)}


def pre_order(node: str):
    if node == '.':
        return
    print(node, end='')
    pre_order(left_tree[alpha_dict[node]])
    pre_order(right_tree[alpha_dict[node]])


def in_order(node: str):
    if node == '.':
        return
    in_order(left_tree[alpha_dict[node]])
    print(node, end='')
    in_order(right_tree[alpha_dict[node]])


def post_order(node: str):
    if node == '.':
        return
    post_order(left_tree[alpha_dict[node]])
    post_order(right_tree[alpha_dict[node]])
    print(node, end='')


Node = int(sys.stdin.readline())

left_tree = ['.'] * 26
right_tree = ['.'] * 26
parent = [0] * 26 

for _ in range(Node):
    root, left, right = sys.stdin.readline().split()
    idx = alpha_dict[root]
    left_tree[idx] = left
    right_tree[idx] = right
    if left != '.':
        parent[alpha_dict[left]] = 1
    if right != '.':
        parent[alpha_dict[right]] = 1

root_node = '.'
for ch, i in alpha_dict.items():
    if parent[i] == 0 and (left_tree[i] != '.' or right_tree[i] != '.' or ch == 'A'):
        root_node = ch
        break

pre_order(root_node)
print()
in_order(root_node)
print()
post_order(root_node)
print()
