import sys

input = sys.stdin.readline

n, m = map(int, input().split())
budget = [int(input()) for _ in range(n)]
start = max(budget)
end = sum(budget)
answer = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    x = mid
    for money in budget:
        if money > x:
            cnt += 1
            x = mid
        x -= money
    if cnt <= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
