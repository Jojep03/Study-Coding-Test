import sys

input = sys.stdin.readline

n, m, p = map(int, input().split())
cnt = 1

score = []
if n > 0:
    score = list(map(int, input().split()))

if n == p and m <= score[-1]:
    print(-1)
else:
    for x in score:
        if x > m:
            cnt += 1
    print(cnt)