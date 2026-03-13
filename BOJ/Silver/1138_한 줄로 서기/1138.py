import sys

input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
x = []

for i in range(n - 1, -1, -1):
    x.insert(line[i], i + 1)
print(*x)


