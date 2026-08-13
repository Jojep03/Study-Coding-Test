import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
left = 0
right = n - 1
res_left = left
res_right = right
res = lst[res_left] + lst[res_right]
while left < right:
    temp = lst[left] + lst[right]
    if abs(temp) < abs(res):
        res_left = left
        res_right = right
        res = temp
    if temp < 0:
        left += 1
    elif temp > 0:
        right -= 1
    else:
        break
print(lst[res_left], lst[res_right])