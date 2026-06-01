import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    card = int(input())
    cards.append(card)
heapq.heapify(cards)
res = 0
for _ in range(n - 1):
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    third = first + second
    res += third
    heapq.heappush(cards, third)
print(res)