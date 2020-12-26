# C(목표인원) N(도시개수)
# 비용  기댓값

import sys
import math


def calculate(n, rule):
    multiplier = math.ceil(n / rule[1])
    return rule[0] * multiplier


def dp(c, n, rules):
    dp = [9999999 for _ in range(c+1)]
    dp[0] = 0
    for rule in rules:
        if dp[1] > rule[1]:
            dp[1] = rule[1]

    for i in range(1, c + 1, 1):
        for rule in rules:
            cost = calculate(i, rule)
            value = min(dp[i - 1] + rule[0], cost)
            dp[i] = min(dp[i], value)

    print(dp)
    print(dp[c])


if __name__ == "__main__":
    C, N = map(int, sys.stdin.readline().split())
    rules = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dp(C, N, rules)