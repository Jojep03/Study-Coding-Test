import sys

input = sys.stdin.readline

n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
min_price = price[0]

price_check = {pri: 0 for pri in price}
for i in range(n- 1):
    min_price = min(min_price, price[i])
    ans += length[i] * min_price
    # price_check[min_price] += 1 #구간개수
    # price_check[min_price] += length[i] #거리 수
print(price_check)
print(ans)

