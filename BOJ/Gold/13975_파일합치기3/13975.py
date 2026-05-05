import heapq
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    files = map(int, input().split())
    res = 0
    heap = []
    for file in files:
        heapq.heappush(heap, file)

    for _ in range(k - 1):
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        cost = first + second
        res += cost
        heapq.heappush(heap, cost)
    print(res)
