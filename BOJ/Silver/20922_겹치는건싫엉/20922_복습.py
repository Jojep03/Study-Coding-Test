import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
cnt = [0] * (max(lst) + 1)
left, right = 0, 0
res = 0
while right < n:
    if cnt[lst[right]] < k:
        cnt[lst[right]] += 1
        right += 1
        res = max(res, right - left)
    else:
        cnt[lst[left]] -= 1
        left += 1
print(res)