code ={
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9
}

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    info = [input().strip() for _ in range(N)]

    include_cypher = ""

    for cypher in info:
        if '1' in cypher:
            include_cypher = cypher
            break

    end = include_cypher.rfind('1')
    start = end - 56 + 1

    find_cypher = include_cypher[start:end+1]

    password = []

    for i in range(0, 56, 7):
        num = find_cypher[i:i+7]
        password.append(code[num])

    result = 0
    print_result = 0
    for j in range(8):
        print_result += password[j]
        if j % 2 == 0:
            result += 3 * password[j]
        else:
            result += password[j]

    total = print_result if result % 10 == 0 else 0

    print(f"#{t} {total}")