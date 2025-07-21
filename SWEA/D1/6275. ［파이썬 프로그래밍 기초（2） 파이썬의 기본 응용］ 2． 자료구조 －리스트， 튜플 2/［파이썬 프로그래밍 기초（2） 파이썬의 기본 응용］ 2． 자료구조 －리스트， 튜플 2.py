text = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
vowel = ['a', 'e', 'i', 'o', 'u']

del_text = [i for i in text if i not in vowel]

print("".join(del_text))