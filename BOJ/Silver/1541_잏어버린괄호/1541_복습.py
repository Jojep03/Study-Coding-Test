import sys

input = sys.stdin.readline

n = input().split("-")
res = sum(map(int, n[0].split("+")))
for x in n[1:]:
    res -= sum(map(int, x.split("+")))
print(res)