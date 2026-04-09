import sys
import math

input = sys.stdin.readline

n = int(input())
m = int(input())
x = list(map(int, input().split()))

a = 0
for i in range(m - 1):
    gap = x[i + 1] - x[i]
    a = max(a, math.ceil(gap / 2))

b = max(x[0], n - x[-1])
print(max(a, b))