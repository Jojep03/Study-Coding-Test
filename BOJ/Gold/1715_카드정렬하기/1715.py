import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    i = int(input())
    heapq.heappush(heap, i)

res = 0
for _ in range(n - 1):
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    res += first + second
    heapq.heappush(heap, first + second)

print(res)