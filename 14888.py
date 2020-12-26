import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))

minv = 1000000001
maxv = -1000000001

def dfs(index, add, sub, mul, div, value):
    global n, minv, maxv
    if index == n:
        minv = min(minv, value)
        maxv = max(maxv, value)
        return
    else:
        if add:
            dfs(index + 1, add - 1, sub, mul, div, value + numbers[index])
        if sub:
            dfs(index + 1, add, sub - 1, mul, div, value - numbers[index])
        if mul:
            dfs(index + 1, add, sub, mul - 1, div, value * numbers[index])
        if div:
            if value < 0:
                output = -(-value // numbers[index])
            else:
                output = value // numbers[index]
            dfs(index + 1, add, sub, mul, div -1, output)

dfs(1, operators[0], operators[1], operators[2], operators[3], numbers[0])

print(maxv)
print(minv)