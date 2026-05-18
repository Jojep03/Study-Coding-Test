import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    alp = input().split()
    print(' '.join(word[::-1] for word in alp))