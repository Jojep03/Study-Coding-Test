import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

l = int(input())
turns = deque()
for _ in range(l):
    x, d = input().split()
    turns.append((int(x), d))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
di = 0

snake = deque([(0, 0)])
snake_set = set([(0, 0)])
time = 0

while True:
    time += 1
    head_x, head_y = snake[0]
    nx = head_x + dx[di]
    ny = head_y + dy[di]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        break

    tail_x, tail_y = snake[-1]
    if (nx, ny) in snake_set and (nx, ny) != (tail_x, tail_y):
        break

    snake.appendleft((nx, ny))
    snake_set.add((nx, ny))

    if board[nx][ny] == 1:
        board[nx][ny] = 0
    else:
        tx, ty = snake.pop()
        snake_set.remove((tx, ty))
        if len(snake) != len(snake_set):
            break

    if turns and turns[0][0] == time:
        _, d = turns.popleft()
        if d == "D":
            di = (di + 1) % 4
        else:
            di = (di - 1) % 4
print(time)

