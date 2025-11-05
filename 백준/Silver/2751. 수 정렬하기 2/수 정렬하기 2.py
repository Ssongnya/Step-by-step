import sys
input = sys.stdin.readline

nums = []

N = int(input())

for _ in range(N):
    nums.append(int(input()))

nums.sort()
for i in nums:
    print(i)