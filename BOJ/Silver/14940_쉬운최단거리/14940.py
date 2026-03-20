import sys
from collections import deque,defaultdict

n, m = map(int, input().split())

lst = []
start = []
for i in range(n):
    a = list(map(int, input().split()))
    lst.append(a)
    if 2 in a:
        start.append((i, a.index(2)))

print(lst)
print(start)
def bfs(graph, start):
    visited = [False] * (n + 1)
    order = []
    stack = deque([start])

    while stack:
        node = stack.popleft()
        if not visited[node]:
            visited[node] = True
            order.append(node)
            for nxt in graph[node]:
                if not visited[nxt]:
                    stack.append(nxt)
    return order