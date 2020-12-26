import sys

n = int(sys.stdin.readline())
sys.setrecursionlimit(10**6)
dpm = [0] * 1001
dpm[1] = 1
dpm[2] = 2
def dp(x):
    if x <= 0:
        return dpm[0]
    if x == 1:
        return dpm[1]
    if x == 2:
        return dpm[2]
    if (dpm[x] != 0):
        return dpm[x]
    dpm[x] = dp(x-1) + dp(x-2)
    return dpm[x]

print(dp(n) % 10007)