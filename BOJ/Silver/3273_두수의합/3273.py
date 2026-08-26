import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
x = int(input())

lst.sort()
left = 0
right = n - 1
cnt = 0
while left < right:
    temp = lst[left] + lst[right]
    if temp > x:
        right -= 1
    elif temp < x:
        left += 1
    else:
        cnt += 1
        left += 1
        right -= 1
print(cnt)
