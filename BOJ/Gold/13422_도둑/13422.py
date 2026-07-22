import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    homes = list(map(int, input().split()))
    temp = sum(homes[:m])
    cnt = 0

    if n == m:
        if temp < k:
            cnt += 1
    else:
        for i in range(n):
            if temp < k:
                cnt += 1
            temp -= homes[i]
            temp += homes[(i + m) % n]
    print(cnt)