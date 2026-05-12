import sys
from collections import defaultdict, deque


input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

def dfs(graph, start):
    visited = [False] * (n + 1)
    order = []
    stack = deque([start])

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            order.append(node)
            for next in reversed(graph[node]):
                if not visited[next]:
                    stack.append(next)
    return order
print(*dfs(graph, v))

def bfs(graph, start):
    visited = [False] * (n + 1)
    order = []
    stack = deque([start])

    while stack:
        node = stack.popleft()
        if not visited[node]:
            visited[node] = True
            order.append(node)
            for next in graph[node]:
                if not visited[next]:
                    stack.append(next)
    return order
print(*bfs(graph, v))