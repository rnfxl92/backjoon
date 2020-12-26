g = int(input())

start = 1
end = 1

exist = False

while True:
    if (end * end - start * start == g) :
        exist = True
        print(end)
    if (end - start == 1) and (end * end - start * start > g):
        break
    if end * end - start * start > g:
        start += 1
    else: end += 1
if exist == False:
    print(-1)
