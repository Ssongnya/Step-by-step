T = int(input())

pair = {'b': 'd', 'p': 'q', 'd': 'b', 'q': 'p'}

for t in range(1, T + 1):
    txt = input()

    reverse = [pair[x] for x in txt]
    result = ("".join(reverse))[::-1]
    
    print(f"#{t} {result}")
