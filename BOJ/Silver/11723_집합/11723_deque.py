import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

s = deque()
for _ in range(n):
    cmd = list(input().split())

    if cmd[0] == "add":
        if int(cmd[1]) not in s:
            s.append(int(cmd[1]))

    elif cmd[0] == "remove":
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))

    elif cmd[0] == "toggle":
        x = int(cmd[1])
        if x in s:
            s.remove(x)
        else:
            s.append(x)

    elif cmd[0] == "all":
        s.clear()
        for i in range(1, 21):
            s.append(i)

    elif cmd[0] == "empty":
        s.clear()

    elif cmd[0] == "check":
        print(1 if cmd[1] in s else 0)


