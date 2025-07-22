txt = list(input().split())

sort_txt = sorted(set(txt))

print(",".join(sort_txt))