import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
left = 0
right = n - 1
lst_left = left
lst_right = right
res = lst[lst_left] + lst[lst_right]
while left < right:
    temp = lst[left] + lst[right]
    if abs(temp) < abs(res):
        res = temp
        lst_left = left
        lst_right = right
    if temp < 0:
        left += 1
    elif temp > 0:
        right -= 1
    else:
        lst_left = left
        lst_right = right
        break
print(lst[lst_left], lst[lst_right])