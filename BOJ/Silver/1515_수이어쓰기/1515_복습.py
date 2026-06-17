import sys

input = sys.stdin.readline

n = input().strip()

i = 1
idx = 0
while True:
    for ch in str(i):
        if ch == n[idx]:
            idx += 1
            if idx == len(n):
                print(i)
                exit()
    i += 1
    
