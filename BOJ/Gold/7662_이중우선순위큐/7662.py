import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    q_max = []
    q_min = []
    visited = [False] * k
    for i in range(k):
        cmd, n = input().split()
        n = int(n)

        if cmd == "I":
            heapq.heappush(q_max, (-n, i))
            heapq.heappush(q_min, (n, i))
            visited[i] = True

        elif cmd == "D":
            if n == 1:
                while q_max and not visited[q_max[0][1]]:
                    heapq.heappop(q_max)
                if q_max:
                    visited[q_max[0][1]] = False
                    heapq.heappop(q_max)
            else:
                while q_min and not visited[q_min[0][1]]:
                    heapq.heappop(q_min)
                if q_min:
                    visited[q_min[0][1]] = False
                    heapq.heappop(q_min)

    while q_max and not visited[q_max[0][1]]:
        heapq.heappop(q_max)
    while q_min and not visited[q_min[0][1]]:
        heapq.heappop(q_min)
    if q_max and q_min:
        print(-q_max[0][0], q_min[0][0])
    else:
        print("EMPTY")
