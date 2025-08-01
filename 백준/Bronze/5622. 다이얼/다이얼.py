grandma = input()

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0

for i in grandma :
    for k in dial :
        if i in k :
            time += (dial.index(k) + 3)

print(time)
