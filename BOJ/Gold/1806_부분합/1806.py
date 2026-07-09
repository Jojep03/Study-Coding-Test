import sys

input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))
left = 0
right = 0
res = lst[0]
cnt = n + 1
while left <= right:
    if res >= s:
        cnt = min(cnt, right - left + 1)
        res -= lst[left]
        left += 1
    else:
        right += 1
        if right < n:
            res += lst[right]
        else:
            break
print(0 if cnt == n + 1 else cnt)