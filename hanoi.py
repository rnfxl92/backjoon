import sys
import collections

a = collections.Counter(["test"])
a.ke
n = int(sys.stdin.readline())
cnt = 0
def hanoi(n, from_pos, to_pos, aux_pos):
    global cnt
    if n == 1:
        print(from_pos, '->', to_pos)
        cnt += 1
        return
    hanoi(n-1, from_pos, aux_pos, to_pos)
    print(from_pos, '->', to_pos)
    cnt += 1
    hanoi(n-1, aux_pos, to_pos, from_pos)

hanoi(n, 1, 3, 2)
print(cnt)