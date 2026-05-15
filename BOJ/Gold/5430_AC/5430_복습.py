import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    cmd = input().strip()
    n = int(input())
    arr = input().strip()
    x = arr[1:-1].split(",") if arr != "[]" else []
    deq = deque(x)
    rev = False
    check = True
    for i in cmd:
        if i == "R":
            rev ^= True
        elif i == "D":
            if deq:
                if rev:
                    deq.pop()
                else:
                    deq.popleft()
            else:
                check = False
                break
    if check:
        if rev:
            print("[" + ",".join(reversed(deq)) + "]")
        else:
            print("[" + ",".join(deq) + "]")
    else:
        print("error")