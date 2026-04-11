import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

start = 1
end = max(lines)
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for line in lines:
        cnt += (line // mid)
    if cnt >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)