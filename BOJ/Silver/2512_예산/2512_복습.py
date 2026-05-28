import sys

input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
m = int(input())

start = 0
end = max(budget)
answer = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for money in budget:
        cnt += min(money, mid)
    if cnt <= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)