import sys
import math

input = sys.stdin.readline

n = int(input())
m = int(input())
x = list(map(int, input().split()))

start = x[0]
end = n - x[-1]
y = 0
for i in range(m - 1):
    y = max(y, math.ceil((x[i + 1] - x[i]) / 2))

res = max(start, end, y)
print(res)