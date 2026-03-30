import sys

input = sys.stdin.readline

n = int(input())
s = 0

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "add":
        s |= (1 << int(cmd[1]))

    elif cmd[0] == "remove":
        s &= ~(1 << int(cmd[1]))

    elif cmd[0] == "check":
        print(1 if s & (1 << int(cmd[1])) else 0)

    elif cmd[0] == "toggle":
        s ^= (1 << int(cmd[1]))

    elif cmd[0] == "all":
        s = (1 << 21) - 2

    elif cmd[0] == "empty":
        s = 0
