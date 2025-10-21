n = int(input())
num_list = list(map(int, input().split()))
target = int(input())

num_list.sort(reverse=True)

i = 0
j = n - 1
result = 0

while i < j:
    current_sum = num_list[i] + num_list[j]
    
    if current_sum == target:
        i += 1
        j -= 1
        result += 1
    elif current_sum > target:
        # Sum is too large, move i forward to get a smaller number
        i += 1
    else:
        # Sum is too small, move j backward to get a smaller number
        j -= 1

print(result)