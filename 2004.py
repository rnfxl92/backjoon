import operator as op
from functools import reduce

def nCr(n, r):
     r = min(r, n-r)
     numerator = reduce(op.mul,range(n,n-r, -1))
     denominator = reduce(op.mul, range(1, r+1))
     result = numerator / denominator
     return int(result)

n, m = map(int, input().split())
temp = nCr(n, m)
count = 0
while temp %10 == 0:
    count +=1
    temp //= 10

print(count)
