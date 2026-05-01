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
heapq.heappush(heap, lst[0][1])
for i in range(1, n):
    s, t = lst[i]
    if s < heap[0]:
        heapq.heappush(heap, t)
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, t)
print(len(heap))