from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
x = list(map(int, input().split()))
q = deque(range(1, n + 1))
res = 0
for i in x:
    target = q.index(i)
    if target <= len(q) // 2:
        for _ in range(target):
            q.append(q.popleft())
            res += 1
    else:
        for _ in range(len(q) - target):
            q.appendleft(q.pop())
            res += 1
    q.popleft()
print(res)