import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0]

for i in range(n):
    left = 0
    right = len(dp) - 1

    while left <= right:
        mid = (left + right) // 2

        if dp[mid] < arr[i]:
            left = mid + 1
        else:
            right = mid - 1

    if left >= len(dp):
        dp.append(arr[i])
    else:
        dp[left] = arr[i]

print(len(dp) - 1)