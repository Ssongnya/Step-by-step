T = int(input())


def text_count(txt):
    txt_dict = {}
    for i in txt:
        txt_dict[i] = txt_dict.get(i, 0) + 1
    return txt_dict


for t in range(1, T + 1):
    str1 = text_count(input().strip())
    str2 = text_count(input().strip())

    same_dict = {x: str2[x] for x in str1.keys()}

    max_value = -1

    for j in same_dict:
        if same_dict[j] > max_value:
            max_value = same_dict[j]

    print(f"#{t} {max_value}")