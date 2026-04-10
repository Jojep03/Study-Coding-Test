import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
m = int(input())
#
# x.sort()
# max_x = 0
# if sum(x) > m:
#     for i in range(n):
#         ans = (m - sum(x[:i])) // len(x[i:])
#         max_x = max(max_x, ans)
# else:
#     max_x = max(x)
# print(max_x)

start = 0
end = max(x)
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for budget in x:
        total += min(budget, mid)

    if total <= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)