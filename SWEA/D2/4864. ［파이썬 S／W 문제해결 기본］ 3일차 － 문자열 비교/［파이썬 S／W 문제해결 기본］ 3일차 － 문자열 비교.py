T = int(input())


for t in range(1, T + 1):
    str1 = input()
    str2 = input()

    m = len(str1)
    n = len(str2)

    if m == 0:
        print(f"#{t} 1")
        continue

    lps = [0] * m

    j = 0
    for i in range(1, m):
        while j>0 and str1[i] != str1[j] :
            j = lps[j - 1]
        if str1[i] == str1[j]:
            j += 1
            lps[i] = j

    j = 0
    found = 0
    
    for i in range(n):
        while j > 0 and str2[i] != str1[j]:
            j = lps[j - 1]
        
        if str2[i] == str1[j]:
            j += 1
            if j == m:
                found = 1
                break

    print(f"#{t} {found}") 

    