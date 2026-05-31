import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)
    cnt = 0
    for i in range(k - 1):
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        third = first + second
        cnt += third
        heapq.heappush(heap, third)
    print(cnt)
