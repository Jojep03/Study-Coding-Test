import sys

input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=True)
res = 0
for i in range(n):
    res = max(res, ropes[i] * (i + 1))
print(res)

