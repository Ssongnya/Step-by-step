T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = input()
    nums_dict = {}
    for i in nums:
        if i in nums_dict.keys():
            nums_dict[i] += 1
        else :
            nums_dict[i] = 1

    key_lst = list(nums_dict.keys())
    value_lst = list(nums_dict.values())

    max_idx = 0
    max_value = value_lst[0]

    for j in range(len(value_lst)):
        if value_lst[j] > max_value:
            max_value = value_lst[j]
            max_idx = j
        elif value_lst[j] == max_value :
            if int(key_lst[j]) > int(key_lst[max_idx]):
                max_idx = j

    print(f"#{t} {int(key_lst[max_idx])} {max_value}")