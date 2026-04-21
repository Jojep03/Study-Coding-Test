import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
lst = deque()
for _ in range(n):
    cmd = input().split( )
    if cmd[0] == "push_front":
        lst.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        lst.append(cmd[1])
    elif cmd[0] == "size":
        print(len(lst))
    elif cmd[0] == "empty":
        print(1 if len(lst) == 0 else 0)
    elif cmd[0] == "pop_front":
        print(lst.popleft() if len(lst) != 0 else -1)
    elif cmd[0] == "pop_back":
        print(lst.pop() if len(lst) != 0 else -1)
    elif cmd[0] == "front":
        print(lst[0] if len(lst) != 0 else -1)
    elif cmd[0] == "back":
        print(lst[-1] if len(lst) != 0 else -1)
