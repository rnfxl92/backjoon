import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
d = [0] * 1001

d[1] = 1
d[2] = 3

def dp(x):
    if x == 1:
        return d[1]
    if x == 2:
        return d[2]
    if d[x] != 0:
        return d[x]
    else:
        d[x] = dp(x - 1) + (2 * dp(x - 2))
        return d[x]

print(dp(n)%10007)