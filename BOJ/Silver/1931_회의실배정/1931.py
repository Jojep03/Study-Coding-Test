from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
lst = []
res = []
for _ in range(n):
    st, en = map(int, input().split())
    lst.append((st, en))

# lst.sort()
# for i in range(n):
#     q = deque()
#     q.append(lst[i][1])
#     for j in range(i, n):
#         s, t = lst[j]
#         if q[-1] > s:
#             continue
#         else:
#             q.append(t)
#     res.append(len(q))
# print(max(res))

lst.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = 0
for st, en in lst:
    if st >= end:
        cnt += 1
        end = en
print(cnt)