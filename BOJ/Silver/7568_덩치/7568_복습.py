import sys

input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    w, k = map(int, input().split())
    lst.append((w, k))
res = []
for i in range(n):
    cnt = 1
    target = lst[i]
    for weight, key in lst:
        if target[0] < weight and target[1] < key:
            cnt += 1
    res.append(cnt)
print(*res)