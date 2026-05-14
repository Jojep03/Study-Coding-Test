import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    st, en = map(int, input().split())
    heapq.heappush(heap,(st, en))

rooms = []

while heap:
    s, e = heapq.heappop(heap)
    if rooms and rooms[0] <= s:
        heapq.heappop(rooms)
    heapq.heappush(rooms, e)
print(rooms)
print(len(rooms))