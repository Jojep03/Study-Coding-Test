import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip()
    stack = []
    result = []

    for ch in s:
        if ch != ' ':
            stack.append(ch)
        else:
            while stack:
                result.append(stack.pop())
            result.append(' ')
    while stack:
        result.append(stack.pop())
    print(''.join(result))