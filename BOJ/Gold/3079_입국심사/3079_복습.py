import sys

input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]
start = 1
end = max(times) * m
answer = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for time in times:
        cnt += mid // time
    if cnt >= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)