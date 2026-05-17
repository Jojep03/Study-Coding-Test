import sys

input = sys.stdin.readline

n, c = map(int, input().split())
homes = []
for _ in range(n):
    home = int(input())
    homes.append(home)
homes.sort()

start = 1
#end = max(homes)
end = homes[-1] - homes[0] # 최대 거리 차이
answer = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    first = homes[0]
    for home in homes:
        if home >= first + mid:
            cnt += 1
            first = home

    if cnt >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)