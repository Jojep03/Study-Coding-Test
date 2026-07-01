import sys

input = sys.stdin.readline

# B 재배열 x
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0
for _ in range(n):
    min_a = min(a)
    max_b = max(b)
    res += min_a * max_b
    a.pop(a.index(min_a))
    b.pop(b.index(max_b))
print(res)

# B 재배열 O

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

res = 0
for i in range(n):
    res += a[i] * b[i]

print(res)