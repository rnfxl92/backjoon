
n, m = map(int, input().split())
arr = list(map(int, input().split()))
summary = 0
end = 0
result = 0
for start in range(n):
    while end < n and summary < m:
        summary += arr[end]
        end += 1
    if summary == m:
        result += 1
    summary -= arr[start]
print(result)