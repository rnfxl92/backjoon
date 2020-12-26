import sys
import copy

n, m = map(int, sys.stdin.readline().split())
totalMap = []
for i in range(n):
    totalMap.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
max_result = 0
def bfs():
    global max_result
    copyed = copy.deepcopy(totalMap)
    result = 0
    queue = []

    for i in range(n):
        for j in range(m):
            if copyed[i][j] == 2:
                queue.append([i, j])
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if x >= 0 and y >= 0 and x < n and y < m:
                if copyed[x][y] == 0:
                    copyed[x][y] = 2
                    queue.append([x, y])
    for i in copyed:
        for j in i:
            if j == 0:
                result += 1
    max_result = max(max_result, result)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if totalMap[i][j] == 0:
                totalMap[i][j] = 1
                wall(cnt + 1)
                totalMap[i][j] = 0

wall(0)
print(max_result)




