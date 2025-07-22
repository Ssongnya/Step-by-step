# menu = b|a

# expensive = {(x, y) for (x, y) in menu.items() if y >= 3000}
# print(expensive)
# ---> 순서가 상관이 없다면 집합연산자를 통해 풀이 가능


a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}

hap = {}

hap = dict(b)
hap.update(a)

result = {(x, y) for x, y in hap.items() if y >= 3000}

print(result)