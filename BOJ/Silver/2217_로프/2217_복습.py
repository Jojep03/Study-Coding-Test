import sys

input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)
res = 0
for i in range(n):
    res = max(res, lst[i] * (i + 1))
print(res)