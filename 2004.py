
def div_num(n, k): #각 n!에 있는 k의 갯수를 구함
    result = 0
    while n>0:
        n //= k
        result += n
    return result

n, m = map(int, input().split())

count5 = div_num(n, 5) - div_num(m, 5) - div_num(n-m, 5)
count2 = div_num(n, 2) - div_num(m, 2) - div_num(n-m, 2)
print(min(count2, count5))
