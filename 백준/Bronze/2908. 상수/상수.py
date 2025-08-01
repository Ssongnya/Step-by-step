real = map(str, input().split())

reverse = []

for i in real :
    reverse.append(int(i[::-1]))

print(max(reverse))