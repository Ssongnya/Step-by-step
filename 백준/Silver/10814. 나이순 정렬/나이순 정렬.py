N = int(input())

people = []

for i in range(N):
    age, name = input().split()
    people.append((int(age), i, name))

people.sort()

for age, _, name in people:
    print(age, name)