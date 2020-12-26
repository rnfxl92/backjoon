import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

dist = [-1] * (n + 1)
dist[x] = 0

queue = deque([x])

while queue:
    now = queue.popleft()
    for next in graph[now]:
        if dist[next] == -1:
            dist[next] = dist[now] + 1
            queue.append(next)
for i in range(n+1):
    if dist[i] == k:
        print(i)
if k not in dist:
    print(-1)