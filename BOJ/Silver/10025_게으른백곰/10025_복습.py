import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for _ in range(n):
    gi, xi = map(int, input().split())
    lst.append((gi, xi))
lst.sort(key=lambda x:x[1])

left = 0
res, temp = 0, 0
for right in range(n):
    lst_g, lst_x = lst[right]
    temp += lst_g
    while lst_x - lst[left][1] > 2 * k:
        temp -= lst[left][0]
        left += 1
    res = max(res, temp)
print(res)

