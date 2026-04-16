import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
lst = deque(i for i in range(1, n + 1))

while len(lst) > 1:
    lst.popleft()
    lst.append(lst.popleft())
print(*lst)