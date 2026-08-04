import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()
left = 0
right = n - 1
res = float("inf")
while right < n:
    temp = lst[right] - lst[left]
    if temp < m:
        right += 1
    else:
        res = min(res, temp)
        if temp == m:
            res = temp
            break
        left += 1
print(res)