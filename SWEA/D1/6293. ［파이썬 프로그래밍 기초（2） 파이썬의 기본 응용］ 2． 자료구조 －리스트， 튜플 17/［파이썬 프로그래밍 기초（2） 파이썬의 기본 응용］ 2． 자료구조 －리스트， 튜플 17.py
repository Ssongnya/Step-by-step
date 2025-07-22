import math

radius = list(map(int, input().split(', ')))
circum =  [f"{2 * i * math.pi:.2f}" for i in radius]

print(", ".join(circum))