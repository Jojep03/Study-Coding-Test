import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
res = []

for i in range(n - 1, -1, -1):
    res.insert(lst[i], i + 1)
print(res)