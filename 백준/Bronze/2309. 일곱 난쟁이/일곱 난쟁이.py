height = [int(input()) for _ in range(9)]
height.sort()

hap = sum(height)
found = False

for i in range(8):
    for j in range(i + 1, 9):
        if hap - height[i] - height[j] == 100:
            del1 = height[i]
            del2 = height[j]
            found = True
            break
    if found:
        break

height.remove(del1)
height.remove(del2)

print(*height, sep="\n")

