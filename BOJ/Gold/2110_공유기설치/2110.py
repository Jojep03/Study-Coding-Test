# 1 2 x x x x x 8 9
# C             C c
import sys

input = sys.stdin.readline

n, c = map(int, input().split())
homes = []
for _ in range(n):
    x = int(input())
    homes.append(x)
homes.sort()

start = 1
end = homes[-1] - homes[0]
answer = 0
while start <= end:
    cnt = 1
    mid = (start + end) // 2
    first = homes[0]

    for home in homes:
        if home >= first + mid:
            first = home
            cnt += 1

    if cnt >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)