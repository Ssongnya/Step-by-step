import sys


def num(start):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, N + 1):
        if i not in arr:
            arr.append(i)
            num(i + 1)
            arr.pop()


N, M = map(int, sys.stdin.readline().split())
arr = []
num(1)
