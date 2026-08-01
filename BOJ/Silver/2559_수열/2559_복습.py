import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
temp = sum(lst[:k])
res = temp
for i in range(k, n):
    temp -= lst[i - k]
    temp += lst[i]
    res = max(temp, res)
print(res)