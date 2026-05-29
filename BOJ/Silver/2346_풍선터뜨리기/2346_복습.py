import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
y = list(map(int, input().split()))
x = deque()
for i in range(n):
    x.append((i + 1, y[i]))
lst = []
# while x:
#     first = x[0]
#     lst.append(y.index(first) + 1)
#     x.popleft()
#     if first > 0:
#         for _ in range(first - 1):
#             if x:
#                 x.append(x.popleft())
#     else:
#         for _ in range(abs(first)):
#             if x:
#                 x.appendleft(x.pop())
while x:
    idx, move = x.popleft()
    lst.append(idx)
    if not x:
        break
    if move > 0:
        for _ in range(move - 1):
            x.append(x.popleft())
    else:
        for _ in range(abs(move)):
            x.appendleft(x.pop())
print(*lst)

