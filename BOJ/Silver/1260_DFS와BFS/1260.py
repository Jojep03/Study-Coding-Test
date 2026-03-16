import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, m, v = map(int, input().split())
# graph = defaultdict(list)
# for _ in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)
# print(graph)
#
# for i in range(1, n + 1):
#     graph[i].sort()
#
# def dfs(graph, start):
#     visited = [False] * (n + 1)
#     order = []
#     stack = deque([start])
#
#     while stack:
#         node = stack.pop()
#         if not visited[node]:
#             visited[node] = True
#             order.append(node)
#             for nxt in reversed(graph[node]):
#                 if not visited[nxt]:
#                     stack.append(nxt)
#     return order
#
# def bfs(graph, start):
#     visited = [False] * (n + 1)
#     order = []
#     stack = deque([start])
#     while stack:
#         node = stack.popleft()
#         if not visited[node]:
#             visited[node] = True
#             order.append(node)
#             for nxt in graph[node]:
#                 if not visited[nxt]:
#                     stack.append(nxt)
#     return order
# print(*dfs(graph, v))
# print(*bfs(graph, v))

graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

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
            for nxt in reversed(graph[node]):
                if not visited[nxt]:
                    stack.append(nxt)
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
            for nxt in graph[node]:
                if not visited[nxt]:
                    stack.append(nxt)
    return order
print(*bfs(graph, v))