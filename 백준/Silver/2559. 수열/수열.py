N, K = map(int, input().split())
weather = list(map(int, input().split()))

hap = sum(weather[:K])
max_weather = hap

for i in range(K, N):
    hap += weather[i] - weather[i - K]
    if hap > max_weather:
        max_weather = hap

print(max_weather)