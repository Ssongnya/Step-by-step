my_str = list(input())

num_up = 0
num_low = 0

for i in range(len(my_str)) :
    if my_str[i].isupper() == True :
        num_up += 1
    elif my_str[i].islower() == True :
        num_low += 1
    else :
        continue

print("UPPER CASE", num_up)
print("LOWER CASE", num_low)