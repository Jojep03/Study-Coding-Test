import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

lst = deque(range(1, n + 1))
res = deque()

while lst:
    for _ in range(k - 1):
        lst.append(lst.popleft())
    res.append(lst.popleft())
print("<" + ", ".join(map(str, res)) + ">")