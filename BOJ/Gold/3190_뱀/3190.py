import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
maps = [[0] * n for _ in range(n)]
for _ in range(k):
    col, row = map(int, input().split())
    maps[col - 1][row - 1] = 1
l = int(input())
rotation = deque()
for _ in range(l):
    x, di = input().split()
    rotation.append((int(x), di))

snake = deque([(0, 0)])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 0
dir = 0
while True:
    #벽 충돌, 몸 충돌
    #머리
    #사과
    #방향 전환

