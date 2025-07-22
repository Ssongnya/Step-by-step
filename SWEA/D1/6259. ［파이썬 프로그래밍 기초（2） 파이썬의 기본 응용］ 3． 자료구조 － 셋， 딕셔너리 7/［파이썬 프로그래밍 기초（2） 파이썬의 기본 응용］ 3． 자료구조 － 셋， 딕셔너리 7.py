text = input()


my_dict = {'LETTERS': 0, 'DIGITS': 0}

for i in text :
    if i.isalpha() :
        my_dict['LETTERS'] += 1
    elif i.isdigit() :
        my_dict['DIGITS'] += 1

print("LETTERS", my_dict['LETTERS'])
print("DIGITS", my_dict['DIGITS'])