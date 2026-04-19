import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
loc = list(map(int, input().split()))

lst = deque(range(1, n + 1))
cnt = 0
for x in loc:
    target = lst.index(x)

    if target <= len(lst) // 2:
        for _ in range(target):
            lst.append(lst.popleft())
            cnt += 1

    else:
        for _ in range(len(lst) - target):
            lst.appendleft(lst.pop())
            cnt += 1

    lst.popleft()
print(cnt)