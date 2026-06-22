import sys

input = sys.stdin.readline

# n = int(input())
# atms = list(map(int, input().split()))
# atms.sort()
# x = atms[0]
# res = atms[0]
# for i in range(1, n):
#     x = x + atms[i]
#     res += x
# print(res)

n = int(input())
atms = sorted(map(int, input().split()))

cur = 0
res = 0
for atm in atms:
    cur += atm
    res += cur
print(res)