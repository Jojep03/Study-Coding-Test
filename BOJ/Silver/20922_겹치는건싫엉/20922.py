import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
left, right = 0, 0
cnt = {i: 0 for i in range(1, n + 1)}
res = 0

while right < n:
    if cnt[lst[right]] < k:
        cnt[lst[right]] += 1
        right += 1
    else:
        cnt[lst[left]] -= 1
        left += 1
    res = max(res, right - left)
print(res)
