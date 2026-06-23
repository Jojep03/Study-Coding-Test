import sys

input = sys.stdin.readline

n = int(input())
res = 0
cnt = 0
while res <= n:
    cnt += 1
    res += cnt
print(cnt - 1)