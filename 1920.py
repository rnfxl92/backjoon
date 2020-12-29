import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())
nArr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mArr = list(map(int, sys.stdin.readline().split()))

nArr.sort()

for i in mArr:
    left = 0
    right = len(nArr) - 1
    check = False
    while left <= right:
        mid = (left + right) // 2

        if i <= nArr[mid]:
            right = mid - 1
            if i == nArr[mid]:
                check = True
                break
        else:
            left = mid + 1

    if check:
        print(1)
    else:
        print(0)
