import sys

input=sys.stdin.readline

N = int(input())
stack = []
commend = []
for i in range(N):
    commend = input().strip().split()
    if commend[0] == "push":
        stack.append(int(commend[1]))
    elif commend[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
    elif commend[0] == "size":
        print(len(stack))
    elif commend[0] == "empty":
        if len(stack) ==0:
            print(1)
        else:
            print(0)
    elif commend[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    else:
        continue



