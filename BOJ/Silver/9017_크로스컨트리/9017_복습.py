import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    players = []
    counter = Counter(lst)
    for player in lst:
        if counter[player] == 6:
            players.append(player)
    res = {}
    idx = 1
    for player in players:
        if player in res:
            if res[player][0] < 4:
                res[player][0] += 1
                res[player][1] += idx
            elif res[player][0] == 4:
                res[player][0] += 1
                res[player][2] = idx
        else:
            res[player] = [1, idx, 0]
        idx += 1
    res = sorted(res.items(), key=lambda x:(x[1][1], x[1][2]))
    print(res[0][0])