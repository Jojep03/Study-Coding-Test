import sys
from collections import deque
input = sys.stdin.readline

# /1 /2 /3 /4 /5 /6 /7
n, k = map(int, input().split())
lst = deque(i for i in range(1, n + 1))
res = deque()

# while len(lst) > k - 1:
#     for _ in range(k - 1):
#         lst.append(lst.popleft())
#     res.append(lst.popleft())
#
# for i in lst:
#     res.append(i)
while lst:
    for _ in range(k - 1):
        lst.append(lst.popleft())
    res.append(lst.popleft())
print("<" + ", ".join(map(str, res)) + ">")