fruit = ['   apple    ','banana','  melon']

result = {x.strip() : len(x.strip()) for x in fruit}

print(result)