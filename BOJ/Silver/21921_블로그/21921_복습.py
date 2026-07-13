import sys

input = sys.stdin.readline

n, x = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
res = sum(lst[:x])
max_res = res
for i in range(x, n):
    res += lst[i]
    res -= lst[i - x]
    if res > max_res:
        max_res = res
        cnt = 1
    elif res == max_res:
        cnt += 1

if max_res == 0:
    print("SAD")
else:
    print(max_res)
    print(cnt)
