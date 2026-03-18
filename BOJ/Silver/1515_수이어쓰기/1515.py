import sys

n = input().strip()

idx = 0
num = 1

while True:
    for ch in str(num):
        if ch == n[idx]:
            idx += 1
            if idx == len(n):
                print(num)
                exit()
    num += 1