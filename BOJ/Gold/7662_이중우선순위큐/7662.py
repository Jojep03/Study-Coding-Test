import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    q_max = []
    q_min = []


    for _ in range(k):
        cmd, n = input().split()
        n = int(n)
        if cmd == "I":
            heapq.heappush(q_max, -n)
            heapq.heappush(q_min, n)
        elif cmd == "D":
            if n == 1:
                if q_max:
                    heapq.heappop(q_max)
            else:
                if q_min:
                    heapq.heappop(q_min)
    if q_max and q_min:
        print(-heapq.heappop(q_max), heapq.heappop(q_min))
    else:
        print("EMPTY")