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
        res = temp
        res_left = left
        res_right = right
        if temp == 0:
            break

    if temp < 0:
        left += 1
    else:
        right -= 1
print(lst[res_left], lst[res_right])