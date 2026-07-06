import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

cnt = sum(visitors[:x])
res = cnt
max_cnt = 1
for i in range(x, n):
    cnt += visitors[i]
    cnt -= visitors[i - x]
    if cnt > res:
        max_cnt = 1
        res = cnt
    elif cnt == res:
        max_cnt += 1

if res == 0:
    print("SAD")
else:
    print(res)
    print(max_cnt)