import sys

input = sys.stdin.readline

n = int(input())

peoples = list(map(int, input().split()))
peoples.sort()

prefix = 0
res = 0
for time in peoples:
    prefix += time
    res += prefix
print(res)