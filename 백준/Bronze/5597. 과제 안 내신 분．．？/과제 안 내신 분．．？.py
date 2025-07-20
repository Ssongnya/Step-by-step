score = [0] * 31

for i in range(1, 31) :
    score[i] = i

for i in range(1, 29):
    n = int(input())
    score.remove(n)

for i in range(2):
    print(score[i+1])