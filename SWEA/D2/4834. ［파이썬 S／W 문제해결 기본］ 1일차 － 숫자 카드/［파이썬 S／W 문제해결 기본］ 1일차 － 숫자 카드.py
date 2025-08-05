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

    max_key = None
    max_value = -1

    for j in nums_dict:
        if nums_dict[j] > max_value:
            max_value = nums_dict[j]
            max_key = j
        elif nums_dict[j] == max_value:
            if int(j) > int(max_key):
                max_key = j

    print(f"#{t} {max_key} {max_value}")