import sys

N = int(sys.stdin.readline())

for _ in range(N):
    stack = 0
    VPS = input()
    for i in range(len(VPS)):
        if VPS[i] == '(' :
            stack += 1
        elif VPS[i] == ')':
            stack -= 1
        if stack < 0 :
            print("NO")
            break
    if stack > 0 :
        print("NO")
    elif stack == 0:
        print("YES")