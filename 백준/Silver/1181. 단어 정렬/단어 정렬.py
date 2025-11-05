N = int(input())

words = []
str_lst = []
for _ in range(N):
    word = input()
    n = len(word)
    if word not in words:
        words.append(word)
        str_lst.append((n, word))

str_lst.sort()

for _, y in str_lst:
    print(y)