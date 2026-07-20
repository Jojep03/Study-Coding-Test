import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
x = [0] * (d + 1)
x[c] = 1
cnt = 1
for i in range(k):
    sushi = lst[i]
    if x[sushi] == 0:
        cnt += 1
    x[sushi] += 1

res = cnt
for i in range(n):
    sushi = lst[i]
    x[sushi] -= 1
    if x[sushi] == 0:
        cnt -= 1
    sushi_ad = lst[(i + k) % n]
    if x[sushi_ad] == 0:
        cnt += 1
    x[sushi_ad] += 1
    res = max(res, cnt)
print(res)