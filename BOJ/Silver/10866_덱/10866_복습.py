import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
deck = deque()
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push_back":
        deck.append(cmd[1])
    elif cmd[0] == "push_front":
        deck.appendleft(cmd[1])
    elif cmd[0] == "pop_front":
        print(deck.popleft() if deck else -1)
    elif cmd[0] == "pop_back":
        print(deck.pop() if deck else -1)
    elif cmd[0] == "size":
        print(len(deck))
    elif cmd[0] == "empty":
        print(0 if deck else 1)
    elif cmd[0] == "front":
        print(deck[0] if deck else -1)
    elif cmd[0] == "back":
        print(deck[-1] if deck else -1)