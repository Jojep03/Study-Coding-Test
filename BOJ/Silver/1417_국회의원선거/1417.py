import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
target = int(input())
for _ in range(n - 1):
    x = int(input())
    heapq.heappush(heap, -x)

res = 0
while heap and -heap[0] >= target:
    vote = -heapq.heappop(heap)
    vote -= 1
    res += 1
    target += 1
    heapq.heappush(heap, -vote)
print(res)