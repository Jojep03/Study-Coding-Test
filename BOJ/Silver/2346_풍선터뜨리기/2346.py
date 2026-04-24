import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
x = list(map(int, input().split()))
y = deque()
for i in range(n):
    y.append((i + 1, x[i]))
res = []
while x:
    idx, target = y.popleft()
    res.append(idx)

    if not y:
        break

    if target > 0:
        for _ in range(target - 1):
            y.append(y.popleft())
    else:
        for _ in range(abs(target)):
            y.appendleft(y.pop())
print(*res)