T = int(input())

for t in range(1, T + 1):
    B, W, X, Y, Z = map(int, input().split())

    if Z * 2 > X + Y:
        mix = min(B, W)
    else:
        mix = 0
    
    score = (B - mix) * X + (W - mix) * Y + 2 * mix * Z
    print(score)