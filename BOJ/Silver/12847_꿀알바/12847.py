import sys

input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))

cnt = sum(t[:m])
res = cnt
for i in range(m, n):
    cnt += t[i]
    cnt -= t[i - m]
    res = max(cnt, res)
print(res)