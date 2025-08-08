#고지식하게 풀어보기

T = int(input())


def brute_force(txt, pattern):
    x, y = len(txt), len(pattern)

    for i in range(x - y + 1):
        match = True
        for j in range(y):
            if txt[i + j] != pattern[j]:
                match = False
                break
        if match:
            return 1

    return 0


for t in range(1, T + 1):

    str1 = input()
    str2 = input()

    result = brute_force(str2, str1)

    print(f"#{t} {result}")