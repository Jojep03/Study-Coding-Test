import sys

input = sys.stdin.readline

n, k = map(int, input().split())

lst = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    lst.append((a, b, c, d))
    if a == k:
        target = (b, c, d)

t_gold, t_silver, t_bronze = target

rank = 1
for _, a, b, c in lst:
    if (a, b, c) > (t_gold, t_silver, t_bronze):
        rank += 1

print(rank)