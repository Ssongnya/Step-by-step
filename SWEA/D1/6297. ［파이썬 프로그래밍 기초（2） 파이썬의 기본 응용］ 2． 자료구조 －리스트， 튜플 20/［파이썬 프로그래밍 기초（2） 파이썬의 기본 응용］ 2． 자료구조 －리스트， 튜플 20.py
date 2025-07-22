nums = list(map(int, input().split(", ")))

odd_nums = [f"{x}" for x in nums if x % 2 == 1]

print(", ".join(odd_nums))