import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    alp = input().strip()
    left = []
    right = []

    for i in alp:
        if i == "<":
            if left:
                right.append(left.pop())
        elif i == ">":
            if right:
                left.append(right.pop())
        elif i == "-":
            if left:
                left.pop()
        else:
            left.append(i)
    print(''.join(left + right[::-1]))