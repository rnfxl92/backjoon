import sys
sys.setrecursionlimit(10**6)

c, n = map(int, sys.stdin.readline().split())

cost = []
customer = []
dp = [10000000000001] * (c+1)
dp[0] = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    cost.append(a)
    customer.append(b)
    dp[b] = min(a, dp[b])

for i in range(1, c+1):
    for j in range(n):
        start = i - customer[j]
        if start < 0:
            start = 0

        dp[i] = min(dp[i], dp[start] + cost[j])


print(dp)
print(dp[c])