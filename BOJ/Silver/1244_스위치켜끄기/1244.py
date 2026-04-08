import sys

input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split()))
m = int(input())
start = 0
end = len(switch) - 1
for _ in range(m):
    s, num = map(int, input().split())
    x = num - 1
    if s == 1:
        for i in range(x, n, num):
            switch[i] ^= 1
    elif s == 2:
        y = min(abs(x - start), abs(x - end))
        switch[x] ^= 1
        for i in range(1, y + 1):
            if switch[x - i] == switch[x + i]:
                switch[x - i] ^= 1
                switch[x + i] ^= 1
            else:
                break

for i in range(n):
    print(switch[i], end=" ")
    if ((i + 1) % 20) == 0:
        print()