import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = input().strip()
    x = arr[1:-1].split(",") if arr != "[]" else []
    lst = deque(x)
    check = True
    rev = False
    for i in p:
        if i == "R":
            rev ^= True
        elif i == "D":
            if len(lst) != 0:
                if rev:
                    lst.pop()
                else:
                    lst.popleft()
            else:
                check = False
                break
    if check:
        if rev:
            lst.reverse()
            print("[" + ",".join(map(str, lst)) + "]")
        else:
            print("[" + ",".join(map(str, lst)) + "]")
    else:
        print("error")