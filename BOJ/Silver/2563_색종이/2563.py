import sys

input = sys.stdin.readline

n = int(input())

papers = []
for _ in range(n):
    x, y = map(int, input().split())
    papers.append((x, y))

board = [[0] * 100 for _ in range(100)]

for x, y in papers:
    target_x = x + 10
    target_y = y + 10
    for i in range(x, target_x):
        for j in range(y, target_y):
            board[i][j] = 1
res = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            res += 1
print(res)
print(sum(map(sum, board)))