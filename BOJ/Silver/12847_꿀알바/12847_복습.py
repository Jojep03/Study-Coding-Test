import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

res = sum(lst[:m])
temp = res
for i in range(m, n):
    temp -= lst[i - m]
    temp += lst[i]
    res = max(res, temp)
print(res)