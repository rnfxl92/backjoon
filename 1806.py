n, m = map(int, input().split())
arr = list(map(int, input().split()))
end = 0
summary = 0
result = m + 1
for start in range(n):
    while end < n and summary < m:
        summary += arr[end]
        end += 1
    if summary >= m:
        if end - start < result:
            result = end - start
    summary -= arr[start]

if result == m + 1:
    print(0)
else:
    print(result)
