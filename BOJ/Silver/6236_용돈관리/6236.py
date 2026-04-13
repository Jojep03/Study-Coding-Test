import sys

input = sys.stdin.readline

n, m = map(int, input().split())
x = [int(input()) for _ in range(n)]

start = max(x)
end = sum(x)
answer = 0

while start <= end:
    mid = (start + end) // 2
    money = mid
    cnt = 1

    for budget in x:
        if money < budget:
            cnt += 1
            money = mid
        money -= budget

    if cnt <= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
