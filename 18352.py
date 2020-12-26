import sys

n, m, k, x = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)

dist = [-1] * (n+1)
dist[x] = 0

queue = [x]
while queue:
    node = queue.pop(0)
    for i in g[node]:
        if dist[i] == -1:
            dist[i] = dist[node] + 1
            queue.append(i)

for i in range(1, n+1):
    if dist[i] == k:
        print(i)

if k not in dist:
    print(-1)