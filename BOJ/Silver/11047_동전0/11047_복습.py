import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)
cnt = 0
for i in lst:
    cnt += k // i
    k %= i
    if k == 0:
        break
print(cnt)