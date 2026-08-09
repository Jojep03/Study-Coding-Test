import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
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
    remove_x = lst[i]
    add_x = lst[(i + k) % n]
    x[remove_x] -= 1
    if x[remove_x] == 0:
        kind -= 1
    if x[add_x] == 0:
        kind += 1
    x[add_x] += 1
    res = max(res, kind)
print(res)