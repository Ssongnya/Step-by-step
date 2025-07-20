nums = [0] * 10
nums_42 = [0] * 10
diff = []

for i in range(10) :
    nums[i] = int(input())
    if nums[i] < 42 :
        nums_42[i] = nums[i]
    else :
        nums_42[i] = nums[i] % 42


for k in nums_42 :
    if k not in diff :
        diff.append(k)

print(len(diff))