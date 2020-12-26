n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()
end = 0
result = 2e9+1
for start in range(n):
    while end < n:
        differ = arr[end] - arr[start]
        if differ < m:
            end += 1
            continue
        if differ >= m:
            result = min(result, differ)
            break
print(result)


