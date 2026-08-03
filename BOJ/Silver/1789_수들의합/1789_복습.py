import sys

input = sys.stdin.readline

s = int(input())
n = 0
cnt = 0
while cnt <= s:
    n += 1
    cnt += n
print(n - 1)