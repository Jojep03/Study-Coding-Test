import sys

input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))
price = list(map(int, input().split()))
min_pri = price[0]
res = 0
for i in range(n - 1):
    min_pri = min(min_pri, price[i])
    res += roads[i] * min_pri
print(res)
