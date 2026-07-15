import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
#ver 1 시간 초과 가능성
# x = {i:0 for i in range(1, d + 1)}
# x[c] = 1
# for i in range(k):
#     x[lst[i]] += 1
# res = sum(1 for value in x.values() if value > 0)
# for i in range(n):
#     x[lst[i]] -= 1
#     x[lst[(i + k) % n]] += 1
#     res = max(res, sum(1 for value in x.values() if value > 0))
# print(res)

#ver 2

x = [0] * (d + 1)
x[c] = 1
kind = 1
for i in range(k):
    sushi = lst[i]
    if x[sushi] == 0:
        kind += 1
    x[sushi] += 1
res = kind

for i in range(n):
    sushi_x = lst[i]
    x[sushi_x] -= 1
    if x[sushi_x] == 0:
        kind -= 1
    sushi_ad = lst[(i + k) % n]
    if x[sushi_ad] == 0:
        kind += 1
    x[sushi_ad] += 1
    res = max(res, kind)
print(res)
