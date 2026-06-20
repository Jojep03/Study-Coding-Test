import sys

input = sys.stdin.readline

n = int(input())
switches = list(map(int, input().split()))
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    s = y - 1
    if x == 1:
        for i in range(s, n, y):
            switches[i] ^= 1
    elif x == 2:
        switches[s] ^= 1
        min_d = min(abs(n - 1 - s), s)
        for i in range(1, min_d + 1):
            if switches[s - i] == switches[s + i]:
                switches[s - i] ^= 1
                switches[s + i] ^= 1
            else:
                break

for i in range(n):
    print(switches[i], end=" ")
    if ((i + 1) % 20) == 0:
        print()
