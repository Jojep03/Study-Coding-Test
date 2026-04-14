import sys

input = sys.stdin.readline
n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]
#
# 0 0 0
# 1 0 7
# 1 1 10
# 2 1 14
# 2 2 20
# 3 2 21
# 4 2 28 최소
# 3 3 30

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