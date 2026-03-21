import sys
from collections import deque,defaultdict

n, m = map(int, input().split())

sy, sx = 0, 0
lst = []
for i in range(n):
    a = list(map(int, input().split()))
    lst.append(a)
    if 2 in a:
        sy, sx = i, a.index(2)

dist = [[-1] * m for _ in range(n)]
# print(dist)
dist[sy][sx] = 0
q = deque()
q.append((sy, sx))
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while q:
    y, x = q.popleft()

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0 <= ny < n and 0 <= nx < m:
            if dist[ny][nx] == -1 and lst[ny][nx] != 0:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))

for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()