import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    lst = deque(range(1, n + 1))
    imp = deque(map(int, input().split()))
    cnt = 0
    target = lst[m]
    while lst:
        max_imp = max(imp)
        for _ in range(imp.index(max_imp)):
            lst.append(lst.popleft())
            imp.append(imp.popleft())
        if lst[0] != target:
            lst.popleft()
            imp.popleft()
            cnt += 1
        else:
            cnt += 1
            break
    print(cnt)
