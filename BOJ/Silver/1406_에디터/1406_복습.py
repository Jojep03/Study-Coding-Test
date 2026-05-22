import sys

input = sys.stdin.readline

left = list(input().split())
right = []
n = int(input())
for _ in range(n):
    cmd = input().split()

    if cmd[0] == "L":
        if left:
            right.append(left.pop())
    elif cmd[0] == "D":
        if right:
            left.append(right.pop())
    elif cmd[0] == "B":
        if left:
            left.pop()
    elif cmd[0] == "P":
        left.append(cmd[1])
print(''.join(left+right[::-1]))
