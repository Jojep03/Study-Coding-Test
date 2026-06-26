import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
res = 0
coins.sort(reverse=True)
for coin in coins:
    if coin <= k:
        cnt = k // coin
        res += cnt
        k -= coin * cnt
        # == k %= coin
print(res)
