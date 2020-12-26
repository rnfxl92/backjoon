
import sys
import math

n = int(sys.stdin.readline())

def prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

prime_Arr = []
for i in range(2, n+1):
    if prime(i):
        prime_Arr.append(i)

end = 0
result = 0
summary = 0
for start in range(len(prime_Arr)):
    while end < len(prime_Arr) and summary < n:
        summary += prime_Arr[end]
        end += 1
    if summary == n:
        result += 1
    summary -= prime_Arr[start]

print(result)