import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    row = list(map(int, input().split()))

    for num in row:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]: #시간초과
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])