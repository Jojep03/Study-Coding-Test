import sys

input = sys.stdin.readline

n = int(input())
lst = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    target_x = x + 10
    target_y = y + 10
    for i in range(x, target_x):
        for j in range(y, target_y):
            lst[i][j] = 1

res = 0
for i in range(100):
    for j in range(100):
        if lst[i][j] == 1:
            res += 1

res2 = sum(map(sum, lst))
print(res)
print(res2)