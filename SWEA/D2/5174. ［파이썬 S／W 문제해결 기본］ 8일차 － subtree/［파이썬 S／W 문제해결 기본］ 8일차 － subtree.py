T = int(input())

def find_child(num, lst):
    count = 1
    for child in lst[num]:
        count += find_child(child, lst)

    return count


for t in range(1, T + 1):
    E, N = map(int, input().split())
    child_lst = list(map(int, input().split()))

    children = [[] for _ in range((E + 2))]
    for i in range(0, len(child_lst), 2):

        parent, child = child_lst[i], child_lst[i + 1]

        children[parent].append(child)
    
    result = find_child(N, children)

    print(f"#{t} {result}")