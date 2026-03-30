import sys
input = sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "add":
        s.add(int(cmd[1]))

    elif cmd[0] == "remove":
        s.discard(int(cmd[1]))

    elif cmd[0] == "check":
        print(1 if int(cmd[1]) in s else 0)

    elif cmd[0] == "toggle":
        x = int(cmd[1])
        if x in s:
            s.remove(x)
        else:
            s.add(x)

    elif cmd[0] == "all":
        s = set(range(1, 21))

    elif cmd[0] == "empty":
        s.clear()