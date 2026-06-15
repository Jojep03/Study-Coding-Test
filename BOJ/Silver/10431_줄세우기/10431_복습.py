import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    case = list(map(int, input().split()))
    ans = 0
    num = case[0]
    heights = case[1:]
    for i in range(20):
        for j in range(i):
            if heights[j] > heights[i]:
                ans += 1
    print(case[0], ans)