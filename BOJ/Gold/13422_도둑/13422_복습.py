import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))

    res = sum(lst[:m])
    temp = res
    cnt = 0

    if n == m:
        if temp < k:
            cnt += 1
    else:
        for i in range(n):
            if temp < k:
                res = max(temp, res)
                cnt += 1
            temp -= lst[i]
            temp += lst[(i + m) % n]
    print(cnt)
    print(res)