import sys

input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))

for i in range(n):
    rank = 1
    target_wei, target_key = lst[i][0], lst[i][1]

    for weight, key in lst:
        if weight > target_wei and key > target_key:
            rank += 1
    print(rank, end=" ")