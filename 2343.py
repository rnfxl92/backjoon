import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left = sum(arr) // m
right = sum(arr)

answer = right

while left <= right:
    mid = (left + right) // 2

    if mid < max(arr):
        left = mid + 1
        continue

    cnt, temp = 0, 0
    for i in range(n):
        if temp + arr[i] <= mid:
            temp += arr[i]
        else:
            temp = arr[i]
            cnt += 1

    if cnt <= m - 1:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)


