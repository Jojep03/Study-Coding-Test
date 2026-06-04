import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
target = None
for _ in range(n):
    a, b, c, d = map(int, input().split())
    lst.append((a, b, c, d))
    if a == k:
        target = (b, c, d)
cnt = 1
for _, b, c, d in lst:
    if (b, c, d) > target:
        cnt += 1
print(cnt)