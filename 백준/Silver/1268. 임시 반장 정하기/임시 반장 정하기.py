N = int(input())

students = [list(map(int, input().split())) for _ in range(N)]

same = [0] * N


for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(5):
            if students[i][k] == students[j][k]:
                same[i] += 1
                break

max_stu = max(same)

for s in range(N):
    if max_stu == same[s]:
        print(s + 1)
        break