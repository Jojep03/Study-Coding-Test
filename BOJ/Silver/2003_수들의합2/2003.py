import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
left = 0
right = 0
cnt = 0
res = 0
while left <= right:
    if res >= m:
        if res == m:
            cnt += 1
        res -= lst[left]
        left += 1
    else:
        if right < n:
            res += lst[right]
            right += 1
        else:
            break
print(cnt)