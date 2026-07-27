import sys

input = sys.stdin.readline

n, l = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
cnt = 0
end = 0

for x in lst:
    if x > end:
        cnt += 1
        end = x + l - 1
print(cnt)