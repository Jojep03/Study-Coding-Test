import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
res = 0
for i in range(n):
    min_a = a[i]
    max_b = max(b)
    res += min_a * max_b
    b.remove(max_b)
print(res)
