fibo = [1, 1]
[fibo.append(fibo[i-2]+fibo[i-1]) for i in range(2, 10)]
print(fibo)