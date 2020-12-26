
n, m, v= map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
DFSvisited = [0] * (n+1)
DFS = []
BFSvisited = [0] * (n+1)
BFS = []
for _ in range(m):
    line = list(map(int, input().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

def dfs(depth):
    if DFSvisited[depth] == 0:
        DFS.append(depth)
        DFSvisited[depth] = 1
        for i in range(1, n+1):
            if(DFSvisited[i] == 0 and matrix[depth][i]):
                dfs(i)

dfs(v)
print(*DFS)

def bfs(v):
    queue = [v]
    BFSvisited[v] = 1
    while(queue):
        v = queue.pop(0)
        BFS.append(v)
        for i in range(1, n+1):
            if BFSvisited[i] == 0 and matrix[v][i] == 1:
                queue.append(i)
                BFSvisited[i] = 1



bfs(v)
print(*BFS)