import math

n, k = map(int, input().split())
prime_ox = [True for _ in range(n + 1)]


num = 1
for i in range(2, n+1):
    if prime_ox[i] == True :
        for j in range(i, n + 1, i):
            if prime_ox[j] == False:
                continue

            if num == k:
                print(j)
            prime_ox[j] = False
            num += 1





