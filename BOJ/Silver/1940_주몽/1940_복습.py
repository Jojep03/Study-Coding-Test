import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
lst = list(map(int, input().split()))
lst.sort()
res = 0
left = 0
right = n - 1
while left < right:
    temp = lst[left] + lst[right]
    if temp < m:
        left += 1
    elif temp > m:
        right -= 1
    else:
        res += 1
        left += 1
        right -= 1
print(res)