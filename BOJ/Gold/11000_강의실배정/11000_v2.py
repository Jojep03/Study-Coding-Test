import sys
import heapq

input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    s, t = map(int, input().split())
    lst.append((s, t))

lst.sort()
heap = []
for s, t in lst:
    if heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, t)
print(len(heap))