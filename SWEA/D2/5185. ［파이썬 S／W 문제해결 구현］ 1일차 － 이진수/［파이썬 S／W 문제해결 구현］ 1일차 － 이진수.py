def hex_to_bin(txt):
    result = bin(int(txt, 16))[2:]
    while len(result) < 4:
        result = '0' + result

    return result


T = int(input())

for t in range(1, T + 1):
    N, text = input().split()

    total = ""

    for i in text:
        total += hex_to_bin(i)

    print(f"#{t} {total}")