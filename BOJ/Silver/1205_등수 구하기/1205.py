import sys
import heapq

input = sys.stdin.readline

n, new, p = map(int,input().split())
if n == 0:
    print(1)

else:
    score = list(map(int, input().split()))
    if n == p and score[-1] >= new:
        print(-1)
    else:
        cnt = 0
        for i in range(n):
            if new < score[i]:
                cnt += 1
            else:
                break
        print(cnt + 1)