import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

cnt = sum(lst[:k])
res = cnt
for i in range(k, n):
    cnt += lst[i]
    cnt -= lst[i - k]
    if cnt > res:
        res = cnt
print(res)