import sys

n = int(sys.stdin.readline())

t = []
p = []
dp = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)
    dp.append(b)

dp.append(0)

for i in range(n-1, -1, -1):
    if i + t[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+t[i]] + p[i])

print(dp[0])
