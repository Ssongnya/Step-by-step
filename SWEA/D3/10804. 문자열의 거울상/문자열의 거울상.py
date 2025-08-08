T = int(input())

pair = {'b': 'd', 'p': 'q', 'd': 'b', 'q': 'p'}

for t in range(1, T + 1):
    txt = input()

    reverse = [pair[x] for x in txt]
    result = []

    for i in range(len(reverse)-1, -1, -1):
        result.append(reverse[i])
    
    result = "".join(result)
    print(f"#{t} {result}")
