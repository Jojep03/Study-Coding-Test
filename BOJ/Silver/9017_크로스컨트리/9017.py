import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    players = list(map(int, input().split()))
    x = set()
    y = []
    for player in players:
        if players.count(player) == 6:
            x.add(player)
            y.append(player)
    for i in x:
        for j in range(len(y)):
            if y[j] == i:
