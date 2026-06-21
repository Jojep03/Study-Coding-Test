import sys

input = sys.stdin.readline

x = input().strip()
split_x = x.split("-")

res = sum(map(int, split_x[0].split("+")))

for y in split_x[1:]:
    res -= sum(map(int, y.split("+")))
print(res)