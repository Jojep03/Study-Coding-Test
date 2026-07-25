import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
cnt = 0

for i in range(n):
    left = 0
    right = n - 1
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        temp = lst[left] + lst[right]
        if temp < lst[i]:
            left += 1
        elif temp > lst[i]:
            right -= 1
        else:
            cnt += 1
            break
print(cnt)