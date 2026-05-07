from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
q = deque(range(1, n + 1))
res = []
while q:
    for _ in range(k - 1):
        q.append(q.popleft())
    res.append(q.popleft())
print("<" + ", ".join(map(str, res)) + ">")